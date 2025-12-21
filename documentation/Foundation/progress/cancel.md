# cancel()

**Framework**: Foundation  
**Kind**: method

Cancels progress tracking.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancel()
```

#### Discussion

This method invokes the block for [`cancellationHandler`](progress/cancellationhandler.md), if there is one, and ensures that any subsequent reads of the [`isCancelled`](progress/iscancelled.md) property return [`true`](https://developer.apple.com/documentation/Swift/true).

If the receiver has suboperations, the system cancels their progress as well.

## See Also

- [func pause()](progress/pause.md)
  Pauses progress tracking.
- [func resume()](progress/resume.md)
  Resumes progress tracking.
- [var resumingHandler: (() -> Void)?](progress/resuminghandler.md)
  The block to invoke when progress resumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/cancel())*