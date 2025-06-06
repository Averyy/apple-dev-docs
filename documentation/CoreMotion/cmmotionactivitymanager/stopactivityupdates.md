# stopActivityUpdates()

**Framework**: Core Motion  
**Kind**: method

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

#### Discussion

Call this method to stop the delivery of updates that you started by calling the [`startActivityUpdates(to:withHandler:)`](cmmotionactivitymanager/startactivityupdates(to:withhandler:).md) method. This method does not stop queries started using the [`queryActivityStarting(from:to:to:withHandler:)`](cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:).md) method.

## See Also

- [func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)](cmmotionactivitymanager/startactivityupdates(to:withhandler:).md)
  Starts the delivery of current motion data updates to your app.
- [typealias CMMotionActivityHandler](cmmotionactivityhandler.md)
  A block that reports the current motion associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates())*