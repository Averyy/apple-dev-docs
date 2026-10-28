# MEEncodedOutgoingMessage

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

An object that contains the signed or encrypted representation of a message’s RFC 2822 data.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEEncodedOutgoingMessage
```

```objc
@interface MEEncodedOutgoingMessage : NSObject
```

## Overview

When MailKit invokes your message security handler’s [`encode(_:composeContext:completionHandler:)`](./memessageencoder/encode%28_,composecontext,completionhandler%29.md) method, it digitally signs and encrypts the message. After encoding the message data, create an instance of [`MEEncodedOutgoingMessage`](./meencodedoutgoingmessage.md) to pass back to MailKit. Set the [`isSigned`](./meencodedoutgoingmessage/issigned.md) and [`isEncrypted`](./meencodedoutgoingmessage/isencrypted.md) values to indicate how you encoded the message.

## Topics

### Encoding Outgoing Messages
- [init(rawData: Data, isSigned: Bool, isEncrypted: Bool)](./meencodedoutgoingmessage/init%28rawdata,issigned,isencrypted%29.md)
  Creates an object that contains the outgoing message’s encoded data, and indicates if the encoder encrypted or signed the message.
- [var isEncrypted: Bool](./meencodedoutgoingmessage/isencrypted.md)
  A Boolean value that indicates if the message encoder encrypted the message.
- [var isSigned: Bool](./meencodedoutgoingmessage/issigned.md)
  A Boolean value that indicates if the message encoder signed the message.
- [var rawData: Data](./meencodedoutgoingmessage/rawdata.md)
  The encrypted, signed, or both encrypted and signed data for the outgoing message.
### Initializers
- [init?(coder: NSCoder)](./meencodedoutgoingmessage/init%28coder%29.md)

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

### Encrypting and Signing Messages
- [protocol MEMessageEncoder](./memessageencoder.md)
  An object that encrypts or digitally signs outgoing messages.
- [class MEOutgoingMessageEncodingStatus](./meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.
- [class MEMessageEncodingResult](./memessageencodingresult.md)
  An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meencodedoutgoingmessage)*