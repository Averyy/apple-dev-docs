# stopStepCountingUpdates()

**Framework**: Core Motion  
**Kind**: method

Stops the delivery of step-counting updates to your app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func stopStepCountingUpdates()
```

#### Discussion

Call this method to stop the delivery of updates that you started by calling the [`startStepCountingUpdates(to:updateOn:withHandler:)`](cmstepcounter/startstepcountingupdates(to:updateon:withhandler:).md) method. This method does not stop queries started using the [`queryStepCountStarting(from:to:to:withHandler:)`](cmstepcounter/querystepcountstarting(from:to:to:withhandler:).md) method.

## See Also

- [func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)](cmstepcounter/startstepcountingupdates(to:updateon:withhandler:).md)
  Starts the delivery of current step-counting data to your app.
- [typealias CMStepUpdateHandler](cmstepupdatehandler.md)
  A block that reports the number of steps recorded since updates began.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates())*