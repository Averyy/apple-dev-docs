# numericCode(length:)

**Framework**: Media Device  
**Kind**: method

Creates a numeric PIN entry authorization method.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static func numericCode(length: MediaOutputDevice.AuthorizationMethod.CodeLength) -> MediaOutputDevice.AuthorizationMethod
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

The system presents a UI with individual digit fields for the user to enter a numeric code when connecting to the device.

```swift
// Present a 4-digit PIN entry UI
let auth = AuthorizationMethod.numericCode(length: .fourCharacter)
```

## Parameters

- `length`: The number of digit fields presented in the pairing UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/authorizationmethod/numericcode(length:))*