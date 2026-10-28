# CMMotionActivityHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(CMMotionActivity *) CMMotionActivityHandler;
```

## Discussion

This block takes the following parameter:

- **`activity`**: The motion activity object that defines the current type of motion for the device.

## See Also

### Starting and Stopping Activity Updates
- [func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)](./cmmotionactivitymanager/startactivityupdates%28to,withhandler%29.md)
  Starts the delivery of current motion data updates to your app.
- [func stopActivityUpdates()](./cmmotionactivitymanager/stopactivityupdates%28%29.md)
  Stops the delivery of motion updates to your app


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)*