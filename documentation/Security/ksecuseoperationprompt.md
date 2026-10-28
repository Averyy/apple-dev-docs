# kSecUseOperationPrompt

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is an operation prompt.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Use kSecUseAuthenticationContext and set LAContext.localizedReason property

## Declaration

```swift
let kSecUseOperationPrompt: CFString
```

```c
extern CFStringRef const kSecUseOperationPrompt;
```

## Discussion

The corresponding value is of type [`CFString`](../CoreFoundation/cfstring.md) and represents a string describing the operation for which the app is attempting to authenticate. When performing user authentication, the system includes the string in the user prompt. The app is responsible for text localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseoperationprompt)*