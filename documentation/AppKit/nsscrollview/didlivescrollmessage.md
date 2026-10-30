# NSScrollView.DidLiveScrollMessage

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct DidLiveScrollMessage
```

## Topics

### Initializers
- [init(scrollView: NSScrollView)](./didlivescrollmessage/init%28scrollview%29.md)
### Instance Properties
- [var scrollView: NSScrollView](./didlivescrollmessage/scrollview.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Notifications
- [class let willStartLiveMagnifyNotification: NSNotification.Name](./willstartlivemagnifynotification.md)
  Posted at the beginning of a magnify gesture.
- [NSScrollView.WillStartLiveMagnifyMessage](./willstartlivemagnifymessage.md)
- [class let didEndLiveMagnifyNotification: NSNotification.Name](./didendlivemagnifynotification.md)
  Posted at the end of a magnify gesture.
- [NSScrollView.DidEndLiveMagnifyMessage](./didendlivemagnifymessage.md)
- [class let willStartLiveScrollNotification: NSNotification.Name](./willstartlivescrollnotification.md)
  Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [NSScrollView.WillStartLiveScrollMessage](./willstartlivescrollmessage.md)
- [class let didLiveScrollNotification: NSNotification.Name](./didlivescrollnotification.md)
  Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [class let didEndLiveScrollNotification: NSNotification.Name](./didendlivescrollnotification.md)
  Posted on the main thread at the end of live scroll tracking.
- [NSScrollView.DidEndLiveScrollMessage](./didendlivescrollmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/didlivescrollmessage)*