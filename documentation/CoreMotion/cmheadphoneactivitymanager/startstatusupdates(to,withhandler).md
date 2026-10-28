# startStatusUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) startStatusUpdatesToQueue:(NSOperationQueue *) queue withHandler:(CMHeadphoneActivityStatusHandler) handler;
```

## Discussion

If a compatible set of headphones is already connected before you call this method, the handler is called with a status update of [`CMHeadphoneActivityManager.Status.connected`](./status/connected.md) for the connected headphones.

## See Also

### Starting and Stopping Updates
- [func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)](./startactivityupdates%28to,withhandler%29.md)
  Starts headphone activity updates, providing data to the given handler through the given queue.
- [func stopActivityUpdates()](./stopactivityupdates%28%29.md)
  Stops headphone activity updates.
- [func stopStatusUpdates()](./stopstatusupdates%28%29.md)
  Stops headphone status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:))*