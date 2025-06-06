# MEDecodedMessage

**Framework**: MailKit  
**Kind**: class

An object that contains the RFC 2822 data for a message, without encryption or digital signatures.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEDecodedMessage
```

#### Overview

When MailKit invokes your message security handler’s [`decodedMessage(forMessageData:)`](memessagedecoder/decodedmessage(formessagedata:).md) method, you decode the message data and return an instance of [`MEDecodedMessage`](medecodedmessage.md) that contains unencrypted MIME data.

## Topics

### Decoding Messages
- [var rawData: Data?](medecodedmessage/rawdata.md)
  The decoded MIME data for a message.
- [var securityInformation: MEMessageSecurityInformation](medecodedmessage/securityinformation.md)
  An object that contains encryption and digital signature information about the message content.
### Initializers
- [init(data: Data?, securityInformation: MEMessageSecurityInformation, context: Data?)](medecodedmessage/init(data:securityinformation:context:).md)
- [init(data: Data?, securityInformation: MEMessageSecurityInformation, context: Data?, banner: MEDecodedMessageBanner?)](medecodedmessage/init(data:securityinformation:context:banner:).md)
### Instance Properties
- [var banner: MEDecodedMessageBanner?](medecodedmessage/banner.md)
- [var context: Data?](medecodedmessage/context.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol MEMessageDecoder](memessagedecoder.md)
  An object that decrypts messages and provides details about digital signatures.
- [class MEMessageSigner](memessagesigner.md)
  An object that contains details about the person who signed a message.
- [class MEMessageSecurityInformation](memessagesecurityinformation.md)
  An object that contains details about a message’s content, such as if it’s encrypted and who digitally signed it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/medecodedmessage)*