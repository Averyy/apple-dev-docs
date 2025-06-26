# MFMailComposeResult

**Framework**: Message UI  
**Kind**: enum

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

## Topics

### Constants
- [MFMailComposeResult.cancelled](mfmailcomposeresult/cancelled.md)
  The user canceled the operation.
- [MFMailComposeResult.saved](mfmailcomposeresult/saved.md)
  The email message was saved in the user’s drafts folder.
- [MFMailComposeResult.sent](mfmailcomposeresult/sent.md)
  The email message was queued in the user’s outbox.
- [MFMailComposeResult.failed](mfmailcomposeresult/failed.md)
  The email message was not saved or queued, possibly due to an error.
### Initializers
- [init?(rawValue: Int)](mfmailcomposeresult/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](mfmailcomposeresult/equatable-implementations.md)
- [RawRepresentable Implementations](mfmailcomposeresult/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func mailComposeController(MFMailComposeViewController, didFinishWith: MFMailComposeResult, error: (any Error)?)](mfmailcomposeviewcontrollerdelegate/mailcomposecontroller(_:didfinishwith:error:).md)
  Tells the delegate that the user wants to dismiss the mail composition view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeresult)*