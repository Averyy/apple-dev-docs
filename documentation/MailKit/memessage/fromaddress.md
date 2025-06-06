# fromAddress

**Framework**: MailKit  
**Kind**: property

The sender’s email address.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@NSCopying
var fromAddress: MEEmailAddress { get }
```

#### Discussion

This property corresponds to the From header in the message.

The value specifies the email address only, and doesn’t include any additional text. For example, if the From header in the message is `Maria Ruiz <mruiz2@icloud.com>`, the value of this property is `mruiz2@icloud.com`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/fromaddress)*