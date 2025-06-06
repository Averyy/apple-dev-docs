# handlerForMessageSecurity()

**Framework**: MailKit  
**Kind**: method

Returns an object that applies security measures such as encryption and digital signatures to messages.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func handlerForMessageSecurity() -> any MEMessageSecurityHandler
```

#### Return Value

An object that encrypts, decrypts, and signs messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextension/handlerformessagesecurity())*