# MEDecodedMessage

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

An object that contains the RFC 2822 data for a message, without encryption or digital signatures.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEDecodedMessage
```

```objc
@interface MEDecodedMessage : NSObject
```

## Overview

When MailKit invokes your message security handler’s [`decodedMessage(forMessageData:)`](./memessagedecoder/decodedmessage%28formessagedata%29.md) method, you decode the message data and return an instance of [`MEDecodedMessage`](./medecodedmessage.md) that contains unencrypted MIME data.

## Topics

### Decoding Messages
- [var rawData: Data?](./medecodedmessage/rawdata.md)
  The decoded MIME data for a message.
- [var securityInformation: MEMessageSecurityInformation](./medecodedmessage/securityinformation.md)
  An object that contains encryption and digital signature information about the message content.
### Initializers
- [init(data: Data?, securityInformation: MEMessageSecurityInformation, context: Data?)](./medecodedmessage/init%28data,securityinformation,context%29.md)
- [init(data: Data?, securityInformation: MEMessageSecurityInformation, context: Data?, banner: MEDecodedMessageBanner?)](./medecodedmessage/init%28data,securityinformation,context,banner%29.md)
- [init?(coder: NSCoder)](./medecodedmessage/init%28coder%29.md)
### Instance Properties
- [var banner: MEDecodedMessageBanner?](./medecodedmessage/banner.md)
- [var context: Data?](./medecodedmessage/context.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Decrypting Messages and Verifying Signatures
- [protocol MEMessageDecoder](./memessagedecoder.md)
  An object that decrypts messages and provides details about digital signatures.
- [class MEMessageSigner](./memessagesigner.md)
  An object that contains details about the person who signed a message.
- [class MEMessageSecurityInformation](./memessagesecurityinformation.md)
  An object that contains details about a message’s content, such as if it’s encrypted and who digitally signed it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/medecodedmessage)*