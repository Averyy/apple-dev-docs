# Media Device

**Framework**: Media Device  
**Kind**: module

Let people stream media from any iOS app to your playback hardware through the media device picker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

#### Overview

Media Device lets you make your playback hardware available to the system. People can then stream to it from any iOS app, selecting your device from the media device picker. The picker is the same UI people use for AirPlay and Bluetooth output. You build a [`MediaDeviceExtension`](mediadeviceextension.md) that the system loads when someone opens the picker, and your extension handles discovery, connection, and playback on behalf of the system.

> **Note**: Your extension and the container app require the [`com.apple.developer.media-device-extension`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.media-device-extension) entitlement.

![An illustration showing an external speaker on the left wirelessly connecting to an iPhone on the right. Here, the speaker is an external media device that someone can connect to their iPhone using a Media Device extension.](/images/com.apple.mediadevice/media-device-framework-hero@2x.png)

The extension life cycle follows three phases: discovery, activation, and playback. During discovery, your extension reports available devices to the system through [`MediaDeviceRoutingManager`](mediadeviceroutingmanager.md). Your devices appear in the media device picker that media apps present to people. When someone selects one of your devices, the system creates a [`MediaOutputSession`](mediaoutputsession.md) and asks your extension to connect. After your extension connects and calls [`activatedDevice(_:session:)`](mediadeviceroutingmanager/activateddevice(_:session:).md), the system notifies supporting media apps about the selected device, and they can call playback APIs such as [`startSession(_:identifier:url:)`](mediadeviceextension/startsession(_:identifier:url:).md).

Your extension may also register to receive real-time audio and video samples by conforming to [`RealtimeSampleHandling`](realtimesamplehandling.md). Real-time streaming, including screen mirroring, requires your extension to publish an audio server driver plug-in shortly after the system activates the device; follow [`Creating an Audio Server Driver Plug-in`](https://developer.apple.com/documentation/coreaudio/creating-an-audio-server-driver-plug-in) to create it. To capture video samples, use [`ScreenCaptureKit`](https://developer.apple.com/documentation/screencapturekit).

Media Device works with [`AVSystemRouting`](https://developer.apple.com/documentation/avsystemrouting), which provides the API for media apps. Media apps use [`AVSystemRouteController`](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-18ns8) to observe route changes, and [`AVSystemRoute`](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um) to control playback while your extension handles the protocol-specific communication with the hardware.

## Topics

### Essentials
- [Creating a media device extension](creating-a-media-device-extension.md)
  Provide a way for people to find, connect to, and control your media device by adding a device extension in your iOS app.
- [Routing media to third-party devices](../avsystemrouting/routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [protocol MediaDeviceExtension](mediadeviceextension.md)
  A protocol that defines the requirements of a media device extension that discovers, activates, and plays media on a remote device.
- [protocol MediaDeviceExtensionConfiguration](mediadeviceextensionconfiguration.md)
  Configuration for the app extension.
### Device discovery and management
- [struct MediaOutputDevice](mediaoutputdevice.md)
  Represents a discoverable media output device such as a TV, speaker, or streaming stick.
- [MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct.md)
  Defines the media capabilities supported by a [`MediaOutputDevice`](mediaoutputdevice.md).
- [MediaOutputDevice.DeviceType](mediaoutputdevice/devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](mediaoutputdevice/volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.
- [MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod.md)
  Specifies what kind of authorization UI to present when connecting to a device.
### Session and system communication
- [class MediaOutputSession](mediaoutputsession.md)
  Represents a media output session for playing content on a remote device.
- [class MediaDeviceRoutingManager](mediadeviceroutingmanager.md)
  An object used by a [`MediaDeviceExtension`](mediadeviceextension.md) to report device discovery, state changes, and playback events back to the system.
- [protocol RealtimeSampleHandling](realtimesamplehandling.md)
  A protocol that extends a media device extension to support realtime sample delivery.
- [struct MediaDeviceError](mediadeviceerror.md)
  An error returned by MediaDeviceExtension operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaDevice)*