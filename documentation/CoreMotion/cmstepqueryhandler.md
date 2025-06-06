# CMStepQueryHandler

**Framework**: Core Motion  
**Kind**: typealias

A block that reports the number of steps for a query operation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
typealias CMStepQueryHandler = (Int, (any Error)?) -> Void
```

#### Discussion

This block takes two parameters:

## See Also

- [func queryStepCountStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMStepQueryHandler)](cmstepcounter/querystepcountstarting(from:to:to:withhandler:).md)
  Gathers and returns historical step count data for the specified time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)*