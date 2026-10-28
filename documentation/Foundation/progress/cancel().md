# cancel()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancel;
```

## Discussion

This method invokes the block for [`cancellationHandler`](./cancellationhandler.md), if there is one, and ensures that any subsequent reads of the [`isCancelled`](./iscancelled.md) property return [`true`](../../Swift/true.md).

If the receiver has suboperations, the system cancels their progress as well.

## See Also

### Controlling Progress
- [func pause()](./pause%28%29.md)
  Pauses progress tracking.
- [func resume()](./resume%28%29.md)
  Resumes progress tracking.
- [var resumingHandler: (() -> Void)?](./resuminghandler.md)
  The block to invoke when progress resumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/cancel())*