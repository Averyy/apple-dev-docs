# willStartLiveMagnifyNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted at the beginning of a magnify gesture.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class let willStartLiveMagnifyNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSScrollViewWillStartLiveMagnifyNotification;
```

## Discussion

The notification object is the scroll view performing the magnification.

This notification indicates that the magnification property is being changed due to user action. This may be due to the user performing a pinch gesture or a smart zoom gesture. When animating the magnification value yourself via the object’s animator, this notification is not sent.

To observe this notification using Swift concurrency, use [`NSScrollView.WillStartLiveMagnifyMessage`](./willstartlivemagnifymessage.md).

## See Also

### Notifications
- [NSScrollView.WillStartLiveMagnifyMessage](./willstartlivemagnifymessage.md)
- [class let didEndLiveMagnifyNotification: NSNotification.Name](./didendlivemagnifynotification.md)
  Posted at the end of a magnify gesture.
- [NSScrollView.DidEndLiveMagnifyMessage](./didendlivemagnifymessage.md)
- [class let willStartLiveScrollNotification: NSNotification.Name](./willstartlivescrollnotification.md)
  Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [NSScrollView.WillStartLiveScrollMessage](./willstartlivescrollmessage.md)
- [class let didLiveScrollNotification: NSNotification.Name](./didlivescrollnotification.md)
  Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [NSScrollView.DidLiveScrollMessage](./didlivescrollmessage.md)
- [class let didEndLiveScrollNotification: NSNotification.Name](./didendlivescrollnotification.md)
  Posted on the main thread at the end of live scroll tracking.
- [NSScrollView.DidEndLiveScrollMessage](./didendlivescrollmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/willstartlivemagnifynotification)*