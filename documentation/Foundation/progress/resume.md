# resume()

**Framework**: Foundation  
**Kind**: method

Resumes progress tracking.

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
func resume()
```

#### Discussion

This method invokes the block for [`resumingHandler`](progress/resuminghandler.md), if there is one, and ensures that any subsequent reads of the [`isPaused`](progress/ispaused.md) property return [`false`](https://developer.apple.com/documentation/swift/false).

If the receiver has suboperations, the system resumes their progress as well.

## See Also

- [func cancel()](progress/cancel.md)
  Cancels progress tracking.
- [func pause()](progress/pause.md)
  Pauses progress tracking.
- [var resumingHandler: (() -> Void)?](progress/resuminghandler.md)
  The block to invoke when progress resumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/resume())*