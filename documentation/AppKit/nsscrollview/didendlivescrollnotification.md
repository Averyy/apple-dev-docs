# didEndLiveScrollNotification

**Framework**: AppKit  
**Kind**: property

Posted on the main thread at the end of live scroll tracking.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class let didEndLiveScrollNotification: NSNotification.Name
```

#### Discussion

The notification object is the scroll view performing the scroll.

## See Also

- [class let willStartLiveMagnifyNotification: NSNotification.Name](nsscrollview/willstartlivemagnifynotification.md)
  Posted at the beginning of a magnify gesture.
- [class let didEndLiveMagnifyNotification: NSNotification.Name](nsscrollview/didendlivemagnifynotification.md)
  Posted at the end of a magnify gesture.
- [class let willStartLiveScrollNotification: NSNotification.Name](nsscrollview/willstartlivescrollnotification.md)
  Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [class let didLiveScrollNotification: NSNotification.Name](nsscrollview/didlivescrollnotification.md)
  Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/didendlivescrollnotification)*