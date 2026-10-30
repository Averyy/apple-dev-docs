# didLiveScrollNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class let didLiveScrollNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSScrollViewDidLiveScrollNotification;
```

## Discussion

Some user-initiated scrolls (for example, scrolling using legacy mice) are not bracketed by a “willStart/didEnd” notification pair.

The notification object is the scroll view performing the scroll.

To observe this notification using Swift concurrency, use [`NSScrollView.DidLiveScrollMessage`](./didlivescrollmessage.md).

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
- [NSScrollView.DidLiveScrollMessage](./didlivescrollmessage.md)
- [class let didEndLiveScrollNotification: NSNotification.Name](./didendlivescrollnotification.md)
  Posted on the main thread at the end of live scroll tracking.
- [NSScrollView.DidEndLiveScrollMessage](./didendlivescrollmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/didlivescrollnotification)*