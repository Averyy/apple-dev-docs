# startActivityUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Starts headphone activity updates, providing data to the given handler through the given queue.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func startActivityUpdates(to queue: OperationQueue, withHandler handler: @escaping CMHeadphoneActivityManager.ActivityHandler)
```

## See Also

- [func stopActivityUpdates()](cmheadphoneactivitymanager/stopactivityupdates.md)
  Stops headphone activity updates.
- [func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)](cmheadphoneactivitymanager/startstatusupdates(to:withhandler:).md)
  Starts headphone status updates, providing data to the given handler through the given queue.
- [func stopStatusUpdates()](cmheadphoneactivitymanager/stopstatusupdates.md)
  Stops headphone status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:))*