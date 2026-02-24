# Supporting automatic audio switching for third-party accessories

**Framework**: AudioAccessoryKit

Configure your audio accessory to support seamless audio routing between connected devices.

#### Overview

AudioAccessoryKit lets you provide information to the system to support audio switching. The device’s companion app starts by pairing the device over Bluetooth using AccessorySetupKit.  After successfully pairing, register the device with AudioAccessoryKit, providing a list of the audio accessory device’s capabilities to the system.  For example, during registration, the companion app tells the system whether the device can report its physical placement and whether it supports automatic audio switching.  While someone uses the device, the companion app updates the system about changes to the device, such as when someone puts on a pair of headphones.

#### Pair and Register Your Accessory

Before configuring audio features, pair your accessory using [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit). After pairing completes successfully, you receive an [`ASAccessory`](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessory) object from the system that represents your paired device.  You use that object with AudioAccessoryKit to register the device.

After pairing your accessory with the system, create an [`AccessoryControlDevice`](accessorycontroldevice.md) for your accessory and the capabilities it supports. For automatic audio switching, specify the [`audioSwitching`](accessorycontroldevice/capabilities/audioswitching.md) and [`placement`](accessorycontroldevice/capabilities/placement.md) capabilities, as demonstrated below:

```swift
let accessory: ASAccessory  // The object from pairing your accessory.
let capabilities: AccessoryControlDevice.Capabilities = [.audioSwitching, .placement]
try await AccessoryControlDevice.register(accessory, capabilities)
```

When you register the device, it activates the specified capabilities and the system begins routing audio to your accessory.

#### Update Device Placement

Communicate the current placement of your accessory to support intelligent audio routing by setting  [`devicePlacement`](accessorycontroldevice/configuration-swift.struct/deviceplacement.md). Update the placement when your accessory detects a change in its position.

```swift
let device = AccessoryControlDevice.current(accessory)
var configuration = device.configuration

configuration.devicePlacement = .inEar
try await device.update(configuration)
```

Common placement transitions include moving from [`AccessoryControlDevice.Placement.offHead`](accessorycontroldevice/placement/offhead.md) to [`AccessoryControlDevice.Placement.onHead`](accessorycontroldevice/placement/onhead.md) or [`AccessoryControlDevice.Placement.inEar`](accessorycontroldevice/placement/inear.md) when the someone puts on the accessory, and back to [`AccessoryControlDevice.Placement.offHead`](accessorycontroldevice/placement/offhead.md) when removed.  Continue to provide updates to the system, any time the accessory someone places the accessory in a different position.

#### Provide Connected Audio Source Devices

For accessories that connect to multiple Bluetooth devices, inform the system which devices are currently connected by setting their Bluetooth addresses as the primary or secondary audio device.  Providing this information lets the system route audio from the appropriate source.

```swift
let device = AccessoryControlDevice.current(accessory)
var configuration = device.configuration

let bluetoothID = Data([0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC]
configuration.primaryAudioSourceDeviceIdentifier = bluetoothID
try await device.update(configuration)
```

Update the connected devices when your accessory’s Bluetooth connection state changes, such as when a new device connects or an existing device disconnects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/supporting-automatic-audio-switching)*