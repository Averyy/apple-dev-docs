# isCancelled

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isCancelled) BOOL cancelled;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver has been cancelled, otherwise [`false`](../../Swift/false.md).

If your thread supports cancellation, it should check this property periodically and exit if it ever returns [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [func cancel()](./cancel%28%29.md)
  Changes the cancelled state of the receiver to indicate that it should exit.
### Determining the Thread’s Execution State
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value that indicates whether the receiver is executing.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether the receiver has finished execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/iscancelled)*