# pause()

**Framework**: Foundation  
**Kind**: method

Pauses progress tracking.

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
func pause()
```

#### Discussion

This method invokes the block for [`pausingHandler`](progress/pausinghandler.md), if there is one, and ensures that any subsequent reads of the [`isPaused`](progress/ispaused.md) property return [`true`](https://developer.apple.com/documentation/Swift/true).

If the receiver has suboperations, the system pauses their progress as well.

## See Also

- [func cancel()](progress/cancel.md)
  Cancels progress tracking.
- [func resume()](progress/resume.md)
  Resumes progress tracking.
- [var resumingHandler: (() -> Void)?](progress/resuminghandler.md)
  The block to invoke when progress resumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/pause())*