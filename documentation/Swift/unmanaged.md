# Unmanaged

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

- [Working with Core Foundation Types](./working-with-core-foundation-types.md)

## Overview

When you use this type, you become partially responsible for keeping the object alive.

## Topics

### Instance Methods
- [func autorelease() -> Unmanaged<Instance>](./unmanaged/autorelease%28%29.md)
  Performs an unbalanced autorelease of the object.
- [func release()](./unmanaged/release%28%29.md)
  Performs an unbalanced release of the object.
- [func retain() -> Unmanaged<Instance>](./unmanaged/retain%28%29.md)
  Performs an unbalanced retain of the object.
- [func takeRetainedValue() -> Instance](./unmanaged/takeretainedvalue%28%29.md)
  Gets the value of this unmanaged reference as a managed reference and consumes an unbalanced retain of it.
- [func takeUnretainedValue() -> Instance](./unmanaged/takeunretainedvalue%28%29.md)
  Gets the value of this unmanaged reference as a managed reference without consuming an unbalanced retain of it.
- [func toOpaque() -> UnsafeMutableRawPointer](./unmanaged/toopaque%28%29.md)
  Unsafely converts an unmanaged class reference to a pointer.
### Type Methods
- [static func fromOpaque(UnsafeRawPointer) -> Unmanaged<Instance>](./unmanaged/fromopaque%28_%29.md)
  Unsafely turns an opaque C pointer into an unmanaged class reference.
- [static func passRetained(Instance) -> Unmanaged<Instance>](./unmanaged/passretained%28_%29.md)
  Creates an unmanaged reference with an unbalanced retain.
- [static func passUnretained(Instance) -> Unmanaged<Instance>](./unmanaged/passunretained%28_%29.md)
  Creates an unmanaged reference without performing an unbalanced retain.
### Default Implementations
- [AtomicOptionalRepresentable Implementations](./unmanaged/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](./unmanaged/atomicrepresentable-implementations.md)

## Relationships

### Conforms To
- [AtomicOptionalRepresentable](../Synchronization/atomicoptionalrepresentable.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [Copyable](./copyable.md)
- [Escapable](./escapable.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)

## See Also

### Reference Counting
- [func withExtendedLifetime<T, E, Result>(borrowing T, () throws(E) -> Result) throws(E) -> Result](./withextendedlifetime%28_,_%29-4mmpv.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [func withExtendedLifetime<T, E, Result>(borrowing T, (borrowing T) throws(E) -> Result) throws(E) -> Result](./withextendedlifetime%28_,_%29-59dz3.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [func extendLifetime<T>(borrowing T)](./extendlifetime%28_%29.md)
  Extends the lifetime of the given instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged)*