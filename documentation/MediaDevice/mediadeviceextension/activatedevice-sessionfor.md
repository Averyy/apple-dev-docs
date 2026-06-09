# activateDevice(_:session:for:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when the user activates a device via a user interface.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func activateDevice(_ device: MediaOutputDevice, session: MediaOutputSession, for deviceFeatures: MediaOutputDevice.Capabilities)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

If the device requires additional user authentication, call [`requestPairingCode(for:session:reason:authorizationMethod:)`](mediadeviceroutingmanager/requestpairingcode(for:session:reason:authorizationmethod:).md). The system will report user input via [`connectUsingPairingCode(_:to:session:)`](mediadeviceextension/connectusingpairingcode(_:to:session:).md).

If the authorization fails, or the connection to the device fails, call [`failedToActivateDevice(_:session:error:)`](mediadeviceroutingmanager/failedtoactivatedevice(_:session:error:).md).

If the activation is successful, call [`activatedDevice(_:session:)`](mediadeviceroutingmanager/activateddevice(_:session:).md).

#### Grouping

If the extension receives multiple activations, then the associated [`MediaOutputDevice`](mediaoutputdevice.md) instances should be grouped together. If the devices are already members of a group, then those groups should now be considered grouped together. [`updateDevices(_:)`](mediadeviceroutingmanager/updatedevices(_:).md) should be called to update the state of group information.

## Parameters

- `device`: The device to activate.
- `session`: The session associated with the activation.
- `deviceFeatures`: The capabilities requested for this activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/activatedevice(_:session:for:))*