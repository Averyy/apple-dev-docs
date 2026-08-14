# MFMailComposeError

**Framework**: Message UI  
**Kind**: struct

Mail composition errors.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct MFMailComposeError
```

## Topics

### Errors
- [static var errorDomain: String](mfmailcomposeerror/errordomain.md)
  The domain for errors related to mail composition.
- [static var saveFailed: MFMailComposeError.Code](mfmailcomposeerror/savefailed.md)
  An error occurred while trying to save the email message to the drafts folder.
- [static var sendFailed: MFMailComposeError.Code](mfmailcomposeerror/sendfailed.md)
  An error occurred while trying to queue or send the email message.
- [MFMailComposeError.Code](mfmailcomposeerror/code.md)
  Error codes for [`NSError`](https://developer.apple.com/documentation/foundation/nserror) objects that are associated with the mail composition interface.
### Error Configuration
- [static var errorDomain: String](mfmailcomposeerror/errordomain.md)
  The domain for errors related to mail composition.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let MFMailComposeErrorDomain: String](mfmailcomposeerrordomain.md)
  The domain used for error objects that are associated with the mail composition interface.
- [MFMailComposeError.Code](mfmailcomposeerror/code.md)
  Error codes for [`NSError`](https://developer.apple.com/documentation/foundation/nserror) objects that are associated with the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeerror)*