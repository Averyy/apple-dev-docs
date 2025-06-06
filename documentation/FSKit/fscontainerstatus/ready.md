# ready

**Framework**: FSKit  
**Kind**: property

A status that represents a ready container with no error.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class var ready: FSContainerStatus { get }
```

#### Discussion

This value is a [`FSContainerStatus`](fscontainerstatus.md) with a [`state`](fscontainerstatus/state.md) that is [`ready`](fscontainerstatus/ready.md), and a [`status`](fscontainerstatus/status.md) that is `nil`.

## See Also

- [class var active: FSContainerStatus](fscontainerstatus/active.md)
  A status that represents an active container with no error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus/ready)*