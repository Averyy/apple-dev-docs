# MFMailComposeError.Code

**Framework**: Message UI  
**Kind**: enum

Error codes for [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) objects that are associated with the mail composition interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Constants
- [MFMailComposeError.Code.saveFailed](mfmailcomposeerror/code/savefailed.md)
  An error occurred while trying to save the email message to the Drafts folder.
- [MFMailComposeError.Code.sendFailed](mfmailcomposeerror/code/sendfailed.md)
  An error occurred while trying to queue or send the email message.
### Initializers
- [init?(rawValue: Int)](mfmailcomposeerror/code/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](mfmailcomposeerror/code/equatable-implementations.md)
- [RawRepresentable Implementations](mfmailcomposeerror/code/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MFMailComposeError](mfmailcomposeerror.md)
  Mail composition errors.
- [let MFMailComposeErrorDomain: String](mfmailcomposeerrordomain.md)
  The domain used for error objects that are associated with the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/code)*