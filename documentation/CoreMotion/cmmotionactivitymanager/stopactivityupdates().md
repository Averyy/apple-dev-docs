# stopActivityUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops the delivery of motion updates to your app

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func stopActivityUpdates()
```

```objc
- (void) stopActivityUpdates;
```

## Discussion

Call this method to stop the delivery of updates that you started by calling the [`startActivityUpdates(to:withHandler:)`](./startactivityupdates%28to,withhandler%29.md) method. This method does not stop queries started using the [`queryActivityStarting(from:to:to:withHandler:)`](./queryactivitystarting%28from,to,to,withhandler%29.md) method.

## See Also

### Starting and Stopping Activity Updates
- [func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)](./startactivityupdates%28to,withhandler%29.md)
  Starts the delivery of current motion data updates to your app.
- [typealias CMMotionActivityHandler](../cmmotionactivityhandler.md)
  A block that reports the current motion associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates())*