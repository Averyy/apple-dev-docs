# kSecUseOperationPrompt

**Framework**: Security  
**Kind**: var

A key whose value is an operation prompt.

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
let kSecUseOperationPrompt: CFString
```

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and represents a string describing the operation for which the app is attempting to authenticate. When performing user authentication, the system includes the string in the user prompt. The app is responsible for text localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseoperationprompt)*