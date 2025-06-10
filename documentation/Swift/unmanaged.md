# Unmanaged

**Framework**: Swift  
**Kind**: struct

A type for propagating an unmanaged object reference.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Unmanaged<Instance> where Instance : AnyObject
```

## Mentions

- [Working with Core Foundation Types](working-with-core-foundation-types.md)

#### Overview

When you use this type, you become partially responsible for keeping the object alive.

## Topics

### Instance Methods
- [func autorelease() -> Unmanaged<Instance>](unmanaged/autorelease.md)
  Performs an unbalanced autorelease of the object.
- [func release()](unmanaged/release.md)
  Performs an unbalanced release of the object.
- [func retain() -> Unmanaged<Instance>](unmanaged/retain.md)
  Performs an unbalanced retain of the object.
- [func takeRetainedValue() -> Instance](unmanaged/takeretainedvalue.md)
  Gets the value of this unmanaged reference as a managed reference and consumes an unbalanced retain of it.
- [func takeUnretainedValue() -> Instance](unmanaged/takeunretainedvalue.md)
  Gets the value of this unmanaged reference as a managed reference without consuming an unbalanced retain of it.
- [func toOpaque() -> UnsafeMutableRawPointer](unmanaged/toopaque.md)
  Unsafely converts an unmanaged class reference to a pointer.
### Type Methods
- [static func fromOpaque(UnsafeRawPointer) -> Unmanaged<Instance>](unmanaged/fromopaque(_:).md)
  Unsafely turns an opaque C pointer into an unmanaged class reference.
- [static func passRetained(Instance) -> Unmanaged<Instance>](unmanaged/passretained(_:).md)
  Creates an unmanaged reference with an unbalanced retain.
- [static func passUnretained(Instance) -> Unmanaged<Instance>](unmanaged/passunretained(_:).md)
  Creates an unmanaged reference without performing an unbalanced retain.
### Default Implementations
- [AtomicOptionalRepresentable Implementations](unmanaged/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](unmanaged/atomicrepresentable-implementations.md)

## Relationships

### Conforms To
- [AtomicOptionalRepresentable](../synchronization/atomicoptionalrepresentable.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [func withExtendedLifetime<T, E, Result>(borrowing T, () throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-4mmpv.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [func withExtendedLifetime<T, E, Result>(borrowing T, (borrowing T) throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-59dz3.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [func extendLifetime<T>(borrowing T)](extendlifetime(_:).md)
  Extends the lifetime of the given instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged)*