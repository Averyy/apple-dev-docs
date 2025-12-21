# UnsafeForceEffectBuffer

**Framework**: RealityKit  
**Kind**: struct

Provides access to physics body parameters from the effect’s update function or event handler.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct UnsafeForceEffectBuffer<T>
```

#### Overview

This struct is a transient buffer view of underlying data, and is only available in effect’s update function or update closure.

## Topics

### Structures
- [UnsafeForceEffectBuffer.Iterator](unsafeforceeffectbuffer/iterator.md)
  Iterates over all elements of the `UnsafeForceEffectBuffer`.
### Instance Properties
- [var count: Int](unsafeforceeffectbuffer/count.md)
  Returns the number of elements in the buffer.
### Instance Methods
- [func makeIterator() -> UnsafeForceEffectBuffer<T>.Iterator](unsafeforceeffectbuffer/makeiterator.md)
  Returns an iterator for the sequence.
### Subscripts
- [subscript(Int) -> T](unsafeforceeffectbuffer/subscript(_:).md)
  Returns an element by index.

## Relationships

### Conforms To
- [Sequence](../Swift/Sequence.md)

## See Also

- [func update(parameters: inout ForceEffectParameters)](forceeffectprotocol/update(parameters:).md)
  Defines how the custom force effect computes forces at each physics simulation step.
- [static func register(((inout ForceEffectEvent<Self>) -> Void)?)](forceeffectprotocol/register(_:)-1zt9t.md)
  Registers the custom effect.
- [struct PhysicsBodyParameterTypes](physicsbodyparametertypes.md)
  Defines which rigid body inputs are required by a force effect’s update handler.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [struct ForceEffectEvent](forceeffectevent.md)
  A struct that defines the arguments to the custom force effect update closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unsafeforceeffectbuffer)*