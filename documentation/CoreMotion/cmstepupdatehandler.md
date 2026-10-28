# CMStepUpdateHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(long, NSDate *, NSError *) CMStepUpdateHandler;
```

## Discussion

This block takes the following parameters:

- **`numberOfSteps`**: The total number of steps since the [`startStepCountingUpdates(to:updateOn:withHandler:)`](./cmstepcounter/startstepcountingupdates%28to,updateon,withhandler%29.md) method was called.
- **`timestamp`**: The time at which the current step count was reported.
- **`error`**: An error object indicating that there was a problem gathering the data or `nil` if the number of steps was determined correctly.

## See Also

### Starting and Stopping Step Counting Updates
- [func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)](./cmstepcounter/startstepcountingupdates%28to,updateon,withhandler%29.md)
  Starts the delivery of current step-counting data to your app.
- [func stopStepCountingUpdates()](./cmstepcounter/stopstepcountingupdates%28%29.md)
  Stops the delivery of step-counting updates to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)*