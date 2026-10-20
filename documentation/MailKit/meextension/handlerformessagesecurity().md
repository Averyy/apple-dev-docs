# handlerForMessageSecurity()

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method

Returns an object that applies security measures such as encryption and digital signatures to messages.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func handlerForMessageSecurity() -> any MEMessageSecurityHandler
```

```objc
- (id<MEMessageSecurityHandler>) handlerForMessageSecurity;
```

#### Return Value

An object that encrypts, decrypts, and signs messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextension/handlerformessagesecurity())*