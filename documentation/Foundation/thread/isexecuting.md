# isExecuting

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is executing.

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
var isExecuting: Bool { get }
```

```objc
@property (readonly, getter=isExecuting) BOOL executing;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver is executing, otherwise [`false`](../../Swift/false.md).

## See Also

### Determining the Thread’s Execution State
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether the receiver has finished execution.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the receiver is cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/isexecuting)*