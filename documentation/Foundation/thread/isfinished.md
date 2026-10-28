# isFinished

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver has finished execution.

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
var isFinished: Bool { get }
```

```objc
@property (readonly, getter=isFinished) BOOL finished;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver has finished execution, otherwise [`false`](../../Swift/false.md).

## See Also

### Determining the Thread’s Execution State
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value that indicates whether the receiver is executing.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the receiver is cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/isfinished)*