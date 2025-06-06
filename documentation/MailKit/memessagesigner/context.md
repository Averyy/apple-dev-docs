# context

**Framework**: MailKit  
**Kind**: property

Data related to the message signature, such as the signing certificate.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var context: Data { get }
```

## See Also

- [init(emailAddresses: [MEEmailAddress], signatureLabel: String, context: Data?)](memessagesigner/init(emailaddresses:signaturelabel:context:).md)
  Creates a new message signer object that contains the email addresses of the signers, a label, and context data.
- [var emailAddresses: [MEEmailAddress]](memessagesigner/emailaddresses.md)
  An array of email addresses associated with the signature.
- [var label: String](memessagesigner/label.md)
  A string that the message’s headers use to display the message signer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner/context)*