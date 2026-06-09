# requestPairingCode(for:session:reason:authorizationMethod:)

**Framework**: Media Device  
**Kind**: method

Presents a pairing user interface so the user can enter authorization credentials for a device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func requestPairingCode(for device: MediaOutputDevice, session: MediaOutputSession, reason: LocalizedStringResource, authorizationMethod: MediaOutputDevice.AuthorizationMethod)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when the session requires user input for pairing.

## Parameters

- `device`: The device needing authorization.
- `session`: The session associated with the pairing request.
- `reason`: The reason why the user is being asked to input authorization.
- `authorizationMethod`: The type of authorization user interface to present to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/requestpairingcode(for:session:reason:authorizationmethod:))*