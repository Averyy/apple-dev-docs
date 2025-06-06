# MEEncodedOutgoingMessage

**Framework**: MailKit  
**Kind**: class

An object that contains the signed or encrypted representation of a message’s RFC 2822 data.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEEncodedOutgoingMessage
```

#### Overview

When MailKit invokes your message security handler’s [`encode(_:composeContext:completionHandler:)`](memessageencoder/encode(_:composecontext:completionhandler:).md) method, it digitally signs and encrypts the message. After encoding the message data, create an instance of [`MEEncodedOutgoingMessage`](meencodedoutgoingmessage.md) to pass back to MailKit. Set the [`isSigned`](meencodedoutgoingmessage/issigned.md) and [`isEncrypted`](meencodedoutgoingmessage/isencrypted.md) values to indicate how you encoded the message.

## Topics

### Encoding Outgoing Messages
- [init(rawData: Data, isSigned: Bool, isEncrypted: Bool)](meencodedoutgoingmessage/init(rawdata:issigned:isencrypted:).md)
  Creates an object that contains the outgoing message’s encoded data, and indicates if the encoder encrypted or signed the message.
- [var isEncrypted: Bool](meencodedoutgoingmessage/isencrypted.md)
  A Boolean value that indicates if the message encoder encrypted the message.
- [var isSigned: Bool](meencodedoutgoingmessage/issigned.md)
  A Boolean value that indicates if the message encoder signed the message.
- [var rawData: Data](meencodedoutgoingmessage/rawdata.md)
  The encrypted, signed, or both encrypted and signed data for the outgoing message.

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

- [protocol MEMessageEncoder](memessageencoder.md)
  An object that encrypts or digitally signs outgoing messages.
- [class MEOutgoingMessageEncodingStatus](meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.
- [class MEMessageEncodingResult](memessageencodingresult.md)
  An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meencodedoutgoingmessage)*