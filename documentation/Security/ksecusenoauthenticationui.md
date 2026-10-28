# kSecUseNoAuthenticationUI

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean indicating whether to disallow UI authentication.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.11
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the key [`kSecUseAuthenticationUI`](./ksecuseauthenticationui.md) with value [`kSecUseAuthenticationUIFail`](./ksecuseauthenticationuifail.md) instead.

## Declaration

```swift
let kSecUseNoAuthenticationUI: CFString
```

```c
extern CFStringRef const kSecUseNoAuthenticationUI;
```

## Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). If provided with a value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), the error [`errSecInteractionNotAllowed`](./errsecinteractionnotallowed.md) is returned when the item is attempting to authenticate with UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecusenoauthenticationui)*