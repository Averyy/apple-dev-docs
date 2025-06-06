# kSecUseNoAuthenticationUI

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean indicating whether to disallow UI authentication.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecUseNoAuthenticationUI: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). If provided with a value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), the error [`errSecInteractionNotAllowed`](errsecinteractionnotallowed.md) is returned when the item is attempting to authenticate with UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecusenoauthenticationui)*