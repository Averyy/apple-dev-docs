# replyToAddresses

**Framework**: MailKit  
**Kind**: property

An array of email addresses to use when replying to the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var replyToAddresses: [MEEmailAddress] { get }
```

#### Discussion

This property corresponds to the Reply-To header in the message.

The entries in the array specify the email addresses only, and don’t include any additional text. For example, if the Reply-To header in the message includes `Maria Ruiz <mruiz2@icloud.com>`, the array contains `mruiz2@icloud.com`.

## See Also

- [var fromAddress: MEEmailAddress](memessage/fromaddress.md)
  The sender’s email address.
- [var toAddresses: [MEEmailAddress]](memessage/toaddresses.md)
  An array of email addresses for the primary recipients of the message.
- [var ccAddresses: [MEEmailAddress]](memessage/ccaddresses.md)
  An array of email addresses for the secondary recipients of the message.
- [var bccAddresses: [MEEmailAddress]](memessage/bccaddresses.md)
  An array of email addresses for the concealed tertiary recipients of the message.
- [var allRecipientAddresses: [MEEmailAddress]](memessage/allrecipientaddresses.md)
  An array of email addresses for all recipients of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/replytoaddresses)*