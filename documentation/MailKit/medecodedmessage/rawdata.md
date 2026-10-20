# rawData

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

The decoded MIME data for a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var rawData: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * rawData;
```

## See Also

### Decoding Messages
- [var securityInformation: MEMessageSecurityInformation](./securityinformation.md)
  An object that contains encryption and digital signature information about the message content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/medecodedmessage/rawdata)*