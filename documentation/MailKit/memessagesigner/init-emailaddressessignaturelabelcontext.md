# init(emailAddresses:signatureLabel:context:)

**Framework**: MailKit  
**Kind**: init

Creates a new message signer object that contains the email addresses of the signers, a label, and context data.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(emailAddresses: [MEEmailAddress], signatureLabel label: String, context: Data?)
```

## Parameters

- `emailAddresses`: An array of email addresses associated with the signature.
- `label`: The message signer’s label that Mail shows in the message’s headers.
- `context`: Data related to the message signature, such as the signing certificate.

## See Also

- [var emailAddresses: [MEEmailAddress]](memessagesigner/emailaddresses.md)
  An array of email addresses associated with the signature.
- [var label: String](memessagesigner/label.md)
  A string that the message’s headers use to display the message signer.
- [var context: Data](memessagesigner/context.md)
  Data related to the message signature, such as the signing certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner/init(emailaddresses:signaturelabel:context:))*