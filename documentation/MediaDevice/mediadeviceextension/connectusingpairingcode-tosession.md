# connectUsingPairingCode(_:to:session:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called after the user has input their authorization into a user interface. Use the Security framework’s keychain to store any derived key material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func connectUsingPairingCode(_ pairingCode: String?, to device: MediaOutputDevice, session: MediaOutputSession)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

## Parameters

- `pairingCode`: The PIN code or password entered by the user. May be `nil` if the user canceled the pairing process.
- `device`: The device that the pairing response is for.
- `session`: The session associated with the pairing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/connectusingpairingcode(_:to:session:))*