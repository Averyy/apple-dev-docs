# allRecipientAddresses

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

An array of email addresses for all recipients of the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var allRecipientAddresses: [MEEmailAddress] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<MEEmailAddress *> * allRecipientAddresses;
```

#### Discussion

This property contains all values in [`toAddresses`](./toaddresses.md), [`ccAddresses`](./ccaddresses.md), and [`bccAddresses`](./bccaddresses.md).

The entries in the array specify the email addresses only, and don’t include any additional text. For example, if the recipient headers in the message includes `Maria Ruiz <mruiz2@icloud.com>`, the array contains `mruiz2@icloud.com`.

## See Also

### Accessing the Sender and Recipients
- [var fromAddress: MEEmailAddress](./fromaddress.md)
  The sender’s email address.
- [var toAddresses: [MEEmailAddress]](./toaddresses.md)
  An array of email addresses for the primary recipients of the message.
- [var ccAddresses: [MEEmailAddress]](./ccaddresses.md)
  An array of email addresses for the secondary recipients of the message.
- [var bccAddresses: [MEEmailAddress]](./bccaddresses.md)
  An array of email addresses for the concealed tertiary recipients of the message.
- [var replyToAddresses: [MEEmailAddress]](./replytoaddresses.md)
  An array of email addresses to use when replying to the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/allrecipientaddresses)*