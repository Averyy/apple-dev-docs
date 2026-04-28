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
  The domain of the error.
- [static var saveFailed: MFMailComposeError.Code](mfmailcomposeerror/savefailed.md)
  An error occurred while trying to save the email message to the drafts folder.
- [static var sendFailed: MFMailComposeError.Code](mfmailcomposeerror/sendfailed.md)
  An error occurred while trying to queue or send the email message.
- [MFMailComposeError.Code](mfmailcomposeerror/code.md)
  Error codes for [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) objects that are associated with the mail composition interface.
### Error Configuration
- [static var errorDomain: String](mfmailcomposeerror/errordomain.md)
  The domain of the error.
- [var localizedDescription: String](mfmailcomposeerror/localizeddescription.md)
  Retrieve the localized description for this error.
### Default Implementations
- [CustomNSError Implementations](mfmailcomposeerror/customnserror-implementations.md)
- [Equatable Implementations](mfmailcomposeerror/equatable-implementations.md)
- [Error Implementations](mfmailcomposeerror/error-implementations.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let MFMailComposeErrorDomain: String](mfmailcomposeerrordomain.md)
  The domain used for error objects that are associated with the mail composition interface.
- [MFMailComposeError.Code](mfmailcomposeerror/code.md)
  Error codes for [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) objects that are associated with the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeerror)*