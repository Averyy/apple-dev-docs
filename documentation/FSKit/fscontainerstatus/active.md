# active

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A status that represents an active container with no error.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class var active: FSContainerStatus { get }
```

```objc
@property (class, readonly) FSContainerStatus * active;
```

#### Discussion

This value is a [`FSContainerStatus`](../fscontainerstatus.md) with a [`state`](./state.md) that is [`active`](./active.md), and has a [`status`](./status.md) that is `nil`.

## See Also

### Using common status values
- [class var ready: FSContainerStatus](./ready.md)
  A status that represents a ready container with no error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus/active)*