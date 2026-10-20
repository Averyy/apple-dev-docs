# stopStatusUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops headphone status updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func stopStatusUpdates()
```

```objc
- (void) stopStatusUpdates;
```

## See Also

### Starting and Stopping Updates
- [func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)](./startactivityupdates%28to,withhandler%29.md)
  Starts headphone activity updates, providing data to the given handler through the given queue.
- [func stopActivityUpdates()](./stopactivityupdates%28%29.md)
  Stops headphone activity updates.
- [func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)](./startstatusupdates%28to,withhandler%29.md)
  Starts headphone status updates, providing data to the given handler through the given queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates())*