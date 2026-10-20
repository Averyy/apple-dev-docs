# stopStepCountingUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops the delivery of step-counting updates to your app.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CMPedometer instead

## Declaration

```swift
func stopStepCountingUpdates()
```

```objc
- (void) stopStepCountingUpdates;
```

#### Discussion

Call this method to stop the delivery of updates that you started by calling the [`startStepCountingUpdates(to:updateOn:withHandler:)`](./startstepcountingupdates%28to,updateon,withhandler%29.md) method. This method does not stop queries started using the [`queryStepCountStarting(from:to:to:withHandler:)`](./querystepcountstarting%28from,to,to,withhandler%29.md) method.

## See Also

### Starting and Stopping Step Counting Updates
- [func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)](./startstepcountingupdates%28to,updateon,withhandler%29.md)
  Starts the delivery of current step-counting data to your app.
- [typealias CMStepUpdateHandler](../cmstepupdatehandler.md)
  A block that reports the number of steps recorded since updates began.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates())*