# MFMailComposeResult.sent

**Framework**: Message UI  
**Kind**: case  
**Role**: Case

The email message was queued in the user’s outbox.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case sent
```

```c
MFMailComposeResultSent
```

## Discussion

It is ready to send the next time the user connects to email.

## See Also

### Constants
- [MFMailComposeResult.cancelled](./cancelled.md)
  The user canceled the operation.
- [MFMailComposeResult.saved](./saved.md)
  The email message was saved in the user’s drafts folder.
- [MFMailComposeResult.failed](./failed.md)
  The email message was not saved or queued, possibly due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeresult/sent)*