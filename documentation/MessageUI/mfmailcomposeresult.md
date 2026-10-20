# MFMailComposeResult

**Framework**: Message UI  
**Kind**: enum  
**Role**: Enumeration

Result codes returned when the mail composition interface is dismissed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum MFMailComposeResult
```

```c
enum MFMailComposeResult : NSInteger;
```

## Topics

### Constants
- [MFMailComposeResult.cancelled](./mfmailcomposeresult/cancelled.md)
  The user canceled the operation.
- [MFMailComposeResult.saved](./mfmailcomposeresult/saved.md)
  The email message was saved in the user’s drafts folder.
- [MFMailComposeResult.sent](./mfmailcomposeresult/sent.md)
  The email message was queued in the user’s outbox.
- [MFMailComposeResult.failed](./mfmailcomposeresult/failed.md)
  The email message was not saved or queued, possibly due to an error.
### Initializers
- [init?(rawValue: Int)](./mfmailcomposeresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to Email Completion
- [func mailComposeController(MFMailComposeViewController, didFinishWith: MFMailComposeResult, error: (any Error)?)](./mfmailcomposeviewcontrollerdelegate/mailcomposecontroller%28_,didfinishwith,error%29.md)
  Tells the delegate that the user wants to dismiss the mail composition view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeresult)*