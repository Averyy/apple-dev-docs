# CMStepUpdateHandler

**Framework**: Core Motion  
**Kind**: typealias

A block that reports the number of steps recorded since updates began.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
typealias CMStepUpdateHandler = (Int, Date, (any Error)?) -> Void
```

#### Discussion

This block takes the following parameters:

## See Also

- [func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)](cmstepcounter/startstepcountingupdates(to:updateon:withhandler:).md)
  Starts the delivery of current step-counting data to your app.
- [func stopStepCountingUpdates()](cmstepcounter/stopstepcountingupdates.md)
  Stops the delivery of step-counting updates to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)*