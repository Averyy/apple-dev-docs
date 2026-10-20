# startActivityUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) startActivityUpdatesToQueue:(NSOperationQueue *) queue withHandler:(CMHeadphoneActivityHandler) handler;
```

## See Also

### Starting and Stopping Updates
- [func stopActivityUpdates()](./stopactivityupdates%28%29.md)
  Stops headphone activity updates.
- [func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)](./startstatusupdates%28to,withhandler%29.md)
  Starts headphone status updates, providing data to the given handler through the given queue.
- [func stopStatusUpdates()](./stopstatusupdates%28%29.md)
  Stops headphone status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:))*