# context

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

Data related to the message signature, such as the signing certificate.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var context: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * context;
```

## See Also

### Describing Message Signers
- [init(emailAddresses: [MEEmailAddress], signatureLabel: String, context: Data?)](./init%28emailaddresses,signaturelabel,context%29.md)
  Creates a new message signer object that contains the email addresses of the signers, a label, and context data.
- [var emailAddresses: [MEEmailAddress]](./emailaddresses.md)
  An array of email addresses associated with the signature.
- [var label: String](./label.md)
  A string that the message’s headers use to display the message signer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner/context)*