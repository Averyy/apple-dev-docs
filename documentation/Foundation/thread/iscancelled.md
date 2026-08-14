# isCancelled

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver is cancelled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver has been cancelled, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

If your thread supports cancellation, it should check this property periodically and exit if it ever returns [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func cancel()](thread/cancel.md)
  Changes the cancelled state of the receiver to indicate that it should exit.
- [var isExecuting: Bool](thread/isexecuting.md)
  A Boolean value that indicates whether the receiver is executing.
- [var isFinished: Bool](thread/isfinished.md)
  A Boolean value that indicates whether the receiver has finished execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/iscancelled)*