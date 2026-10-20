# state

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the container state, such as ready, active, or blocked.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var state: FSContainerState { get }
```

```objc
@property (readonly) FSContainerState state;
```

## See Also

### Inspecting status properties
- [enum FSContainerState](../fscontainerstate.md)
  An enumeration of container state values.
- [var status: (any Error)?](./status.md)
  An optional error that provides further information about the state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus/state)*