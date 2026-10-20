# status

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

An optional error that provides further information about the state.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var status: (any Error)? { get }
```

```objc
@property (copy, readonly, nullable) NSError * status;
```

## See Also

### Inspecting status properties
- [var state: FSContainerState](./state.md)
  A value that represents the container state, such as ready, active, or blocked.
- [enum FSContainerState](../fscontainerstate.md)
  An enumeration of container state values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus/status)*