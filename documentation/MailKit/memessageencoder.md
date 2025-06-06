# MEMessageEncoder

**Framework**: MailKit  
**Kind**: protocol

An object that encrypts or digitally signs outgoing messages.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol MEMessageEncoder : NSObjectProtocol
```

## Topics

### Instance Methods
- [func encode(MEMessage, composeContext: MEComposeContext, completionHandler: (MEMessageEncodingResult) -> Void)](memessageencoder/encode(_:composecontext:completionhandler:).md)
- [func getEncodingStatus(for: MEMessage, composeContext: MEComposeContext, completionHandler: (MEOutgoingMessageEncodingStatus) -> Void)](memessageencoder/getencodingstatus(for:composecontext:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MEMessageSecurityHandler](memessagesecurityhandler.md)

## See Also

- [class MEEncodedOutgoingMessage](meencodedoutgoingmessage.md)
  An object that contains the signed or encrypted representation of a message’s RFC 2822 data.
- [class MEOutgoingMessageEncodingStatus](meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.
- [class MEMessageEncodingResult](memessageencodingresult.md)
  An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencoder)*