# resume()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) resume;
```

#### Discussion

This method invokes the block for [`resumingHandler`](./resuminghandler.md), if there is one, and ensures that any subsequent reads of the [`isPaused`](./ispaused.md) property return [`false`](../../Swift/false.md).

If the receiver has suboperations, the system resumes their progress as well.

## See Also

### Controlling Progress
- [func cancel()](./cancel%28%29.md)
  Cancels progress tracking.
- [func pause()](./pause%28%29.md)
  Pauses progress tracking.
- [var resumingHandler: (() -> Void)?](./resuminghandler.md)
  The block to invoke when progress resumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/resume())*