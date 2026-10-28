# CMMotionActivityQueryHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

A block that reports the motion updates that occurred between the specified query interval.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
typealias CMMotionActivityQueryHandler = ([CMMotionActivity]?, (any Error)?) -> Void
```

```c
typedef void (^)(NSArray<CMMotionActivity *> *, NSError *) CMMotionActivityQueryHandler;
```

## Discussion

This block takes the following parameters:

- **`activities`**: An array of [`CMMotionActivity`](./cmmotionactivity.md) objects indicating the updates that occurred. The objects in the array are ordered by the time at which they occurred in the specified time interval. Use the [`startDate`](./cmmotionactivity/startdate.md) property in each motion object to determine when the update occurred.
- **`error`**: An error object indicating that there was a problem gathering the data or `nil` if the motion data was determined correctly.

## See Also

### Getting Historical Activity Data
- [func queryActivityStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMMotionActivityQueryHandler)](./cmmotionactivitymanager/queryactivitystarting%28from,to,to,withhandler%29.md)
  Gathers and returns historical motion data for the specified time period


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)*