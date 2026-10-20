# isCancelled

**Framework**: Dispatch  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the work item has been canceled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var isCancelled: Bool { get }
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the work item has been canceled.

## See Also

### Canceling a Work Item
- [func cancel()](./cancel%28%29.md)
  Cancels the current work item asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/iscancelled)*