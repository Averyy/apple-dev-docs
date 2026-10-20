# NotificationQueue.PostingStyle.now

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The notification is posted immediately after coalescing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case now
```

```c
NSPostNow
```

## See Also

### Constants
- [NotificationQueue.PostingStyle.asap](./asap.md)
  The notification is posted at the end of the current notification callout or timer.
- [NotificationQueue.PostingStyle.whenIdle](./whenidle.md)
  The notification is posted when the run loop is idle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/postingstyle/now)*