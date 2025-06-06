# startStatusUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Starts headphone status updates, providing data to the given handler through the given queue.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func startStatusUpdates(to queue: OperationQueue, withHandler handler: @escaping CMHeadphoneActivityManager.StatusHandler)
```

#### Discussion

If a compatible set of headphones is already connected before you call this method, the handler is called with a status update of [`CMHeadphoneActivityManager.Status.connected`](cmheadphoneactivitymanager/status/connected.md) for the connected headphones.

## See Also

- [func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)](cmheadphoneactivitymanager/startactivityupdates(to:withhandler:).md)
  Starts headphone activity updates, providing data to the given handler through the given queue.
- [func stopActivityUpdates()](cmheadphoneactivitymanager/stopactivityupdates.md)
  Stops headphone activity updates.
- [func stopStatusUpdates()](cmheadphoneactivitymanager/stopstatusupdates.md)
  Stops headphone status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:))*