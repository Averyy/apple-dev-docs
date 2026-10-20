# securityInformation

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

An object that contains encryption and digital signature information about the message content.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var securityInformation: MEMessageSecurityInformation { get }
```

```objc
@property (nonatomic, strong, readonly) MEMessageSecurityInformation * securityInformation;
```

## See Also

### Decoding Messages
- [var rawData: Data?](./rawdata.md)
  The decoded MIME data for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/medecodedmessage/securityinformation)*