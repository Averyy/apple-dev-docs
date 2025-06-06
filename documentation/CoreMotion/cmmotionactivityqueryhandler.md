# CMMotionActivityQueryHandler

**Framework**: Core Motion  
**Kind**: typealias

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

#### Discussion

This block takes the following parameters:

## See Also

- [func queryActivityStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMMotionActivityQueryHandler)](cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:).md)
  Gathers and returns historical motion data for the specified time period


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)*