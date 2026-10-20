# init(emailAddresses:signatureLabel:context:)

**Framework**: MailKit  
**Kind**: init  
**Role**: Initializer

Creates a new message signer object that contains the email addresses of the signers, a label, and context data.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(emailAddresses: [MEEmailAddress], signatureLabel label: String, context: Data?)
```

```objc
- (instancetype) initWithEmailAddresses:(NSArray<MEEmailAddress *> *) emailAddresses signatureLabel:(NSString *) label context:(NSData *) context;
```

## Parameters

- `emailAddresses`: An array of email addresses associated with the signature.
- `label`: The message signer’s label that Mail shows in the message’s headers.
- `context`: Data related to the message signature, such as the signing certificate.

## See Also

### Describing Message Signers
- [var emailAddresses: [MEEmailAddress]](./emailaddresses.md)
  An array of email addresses associated with the signature.
- [var label: String](./label.md)
  A string that the message’s headers use to display the message signer.
- [var context: Data](./context.md)
  Data related to the message signature, such as the signing certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner/init(emailaddresses:signaturelabel:context:))*