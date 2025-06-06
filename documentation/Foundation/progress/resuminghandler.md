# resumingHandler

**Framework**: Foundation  
**Kind**: property

The block to invoke when progress resumes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var resumingHandler: (() -> Void)? { get set }
```

#### Discussion

If the receiver is a suboperation of another progress object, the system invokes the [`resumingHandler`](progress/resuminghandler.md) block when pausing the containing progress object.

##### Special Considerations

You’re responsible for resuming any work for the progress object.

You can invoke the resuming handler on any queue. If you must do work on a specific queue, dispatch to that queue from within the resuming handler block.

## See Also

- [func cancel()](progress/cancel.md)
  Cancels progress tracking.
- [func pause()](progress/pause.md)
  Pauses progress tracking.
- [func resume()](progress/resume.md)
  Resumes progress tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/resuminghandler)*