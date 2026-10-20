# invalidRecipients

**Framework**: MailKit  
**Kind**: property  
**Role**: Type Property

An error that indicates one or more of the message’s recipients are invalid.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static var invalidRecipients: MEComposeSessionError.Code { get }
```

## See Also

### Indicating Erroneous States
- [static var invalidBody: MEComposeSessionError.Code](./invalidbody.md)
  An error that indicates the message’s body is invalid.
- [static var invalidHeaders: MEComposeSessionError.Code](./invalidheaders.md)
  An error that indicates one or more of the message’s headers are invalid.
- [let MEComposeSessionErrorDomain: String](../mecomposesessionerrordomain.md)
  A constant for the compose session error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionerror/invalidrecipients)*