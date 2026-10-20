# MFMailComposeError.Code

**Framework**: Message UI  
**Kind**: enum  
**Role**: Enumeration

Error codes for [`NSError`](../../Foundation/nserror.md) objects that are associated with the mail composition interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum MFMailComposeErrorCode : NSInteger;
```

## Topics

### Constants
- [MFMailComposeError.Code.saveFailed](./code/savefailed.md)
  An error occurred while trying to save the email message to the Drafts folder.
- [MFMailComposeError.Code.sendFailed](./code/sendfailed.md)
  An error occurred while trying to queue or send the email message.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to errors
- [struct MFMailComposeError](../mfmailcomposeerror.md)
  Mail composition errors.
- [let MFMailComposeErrorDomain: String](../mfmailcomposeerrordomain.md)
  The domain used for error objects that are associated with the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/code)*