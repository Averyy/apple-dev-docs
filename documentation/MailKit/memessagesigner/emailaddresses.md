# emailAddresses

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

An array of email addresses associated with the signature.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var emailAddresses: [MEEmailAddress] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<MEEmailAddress *> * emailAddresses;
```

## See Also

### Describing Message Signers
- [init(emailAddresses: [MEEmailAddress], signatureLabel: String, context: Data?)](./init%28emailaddresses,signaturelabel,context%29.md)
  Creates a new message signer object that contains the email addresses of the signers, a label, and context data.
- [var label: String](./label.md)
  A string that the message’s headers use to display the message signer.
- [var context: Data](./context.md)
  Data related to the message signature, such as the signing certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner/emailaddresses)*