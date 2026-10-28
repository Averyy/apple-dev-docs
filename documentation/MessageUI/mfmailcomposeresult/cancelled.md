# MFMailComposeResult.cancelled

**Framework**: Message UI  
**Kind**: case  
**Role**: Case

The user canceled the operation.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case cancelled
```

```c
MFMailComposeResultCancelled
```

## Discussion

No email message was queued.

## See Also

### Constants
- [MFMailComposeResult.saved](./saved.md)
  The email message was saved in the user’s drafts folder.
- [MFMailComposeResult.sent](./sent.md)
  The email message was queued in the user’s outbox.
- [MFMailComposeResult.failed](./failed.md)
  The email message was not saved or queued, possibly due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeresult/cancelled)*