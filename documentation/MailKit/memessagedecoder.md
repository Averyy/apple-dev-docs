# MEMessageDecoder

**Framework**: MailKit  
**Kind**: protocol

An object that decrypts messages and provides details about digital signatures.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol MEMessageDecoder : NSObjectProtocol
```

## Topics

### Decrypting Messages and Verifying Signatures
- [func decodedMessage(forMessageData: Data) -> MEDecodedMessage?](memessagedecoder/decodedmessage(formessagedata:).md)
  Decrypts message content and details about digital signatures.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MEMessageSecurityHandler](memessagesecurityhandler.md)

## See Also

- [class MEDecodedMessage](medecodedmessage.md)
  An object that contains the RFC 2822 data for a message, without encryption or digital signatures.
- [class MEMessageSigner](memessagesigner.md)
  An object that contains details about the person who signed a message.
- [class MEMessageSecurityInformation](memessagesecurityinformation.md)
  An object that contains details about a message’s content, such as if it’s encrypted and who digitally signed it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagedecoder)*