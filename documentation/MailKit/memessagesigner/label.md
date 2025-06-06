# label

**Framework**: MailKit  
**Kind**: property

A string that the message’s headers use to display the message signer.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var label: String { get }
```

## See Also

- [init(emailAddresses: [MEEmailAddress], signatureLabel: String, context: Data?)](memessagesigner/init(emailaddresses:signaturelabel:context:).md)
  Creates a new message signer object that contains the email addresses of the signers, a label, and context data.
- [var emailAddresses: [MEEmailAddress]](memessagesigner/emailaddresses.md)
  An array of email addresses associated with the signature.
- [var context: Data](memessagesigner/context.md)
  Data related to the message signature, such as the signing certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner/label)*