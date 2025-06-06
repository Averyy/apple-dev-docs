# CMMotionActivityHandler

**Framework**: Core Motion  
**Kind**: typealias

A block that reports the current motion associated with the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
typealias CMMotionActivityHandler = (CMMotionActivity?) -> Void
```

#### Discussion

This block takes the following parameter:

## See Also

- [func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)](cmmotionactivitymanager/startactivityupdates(to:withhandler:).md)
  Starts the delivery of current motion data updates to your app.
- [func stopActivityUpdates()](cmmotionactivitymanager/stopactivityupdates.md)
  Stops the delivery of motion updates to your app


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)*