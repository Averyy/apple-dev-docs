# MTLPurgeableState

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The purgeable state of the resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum MTLPurgeableState
```

```c
enum MTLPurgeableState : NSUInteger;
```

## Topics

### Specifying purgeable states
- [MTLPurgeableState.keepCurrent](./mtlpurgeablestate/keepcurrent.md)
  The current state is queried but doesn’t change.
- [MTLPurgeableState.nonVolatile](./mtlpurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableState.volatile](./mtlpurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.
- [MTLPurgeableState.empty](./mtlpurgeablestate/empty.md)
  A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.
### Initializers
- [init?(rawValue: UInt)](./mtlpurgeablestate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting the purgeable state of the resource
- [func setPurgeableState(MTLPurgeableState) -> MTLPurgeableState](./mtlresource/setpurgeablestate%28_%29.md)
  Specifies or queries the resource’s purgeable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpurgeablestate)*