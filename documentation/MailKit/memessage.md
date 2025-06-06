# MEMessage

**Framework**: MailKit  
**Kind**: class

An object that contains information about a mail message, such as the subject, addressees, date sent, and the message contents.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessage
```

## Topics

### Accessing the Sender and Recipients
- [var fromAddress: MEEmailAddress](memessage/fromaddress.md)
  The sender’s email address.
- [var toAddresses: [MEEmailAddress]](memessage/toaddresses.md)
  An array of email addresses for the primary recipients of the message.
- [var ccAddresses: [MEEmailAddress]](memessage/ccaddresses.md)
  An array of email addresses for the secondary recipients of the message.
- [var bccAddresses: [MEEmailAddress]](memessage/bccaddresses.md)
  An array of email addresses for the concealed tertiary recipients of the message.
- [var replyToAddresses: [MEEmailAddress]](memessage/replytoaddresses.md)
  An array of email addresses to use when replying to the message.
- [var allRecipientAddresses: [MEEmailAddress]](memessage/allrecipientaddresses.md)
  An array of email addresses for all recipients of the message.
### Accessing the Message Subject
- [var subject: String](memessage/subject.md)
  The subject of the message.
### Accessing Message Content
- [var headers: [String : [String]]?](memessage/headers.md)
  A dictionary that contains the message’s header values.
- [var rawData: Data?](memessage/rawdata.md)
  The raw RFC 2822 header and body content of the message.
### Accessing Message State
- [var state: MEMessageState](memessage/state.md)
  The state of the mail message.
### Instance Properties
- [var encryptionState: MEMessageEncryptionState](memessage/encryptionstate.md)

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

- [enum MEMessageState](memessagestate.md)
  The state of a message: sent, unsent, or received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage)*