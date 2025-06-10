# AtomicLazyReference

**Framework**: Synchronization  
**Kind**: struct

A lazily initializable atomic strong reference.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct AtomicLazyReference<Instance> where Instance : AnyObject
```

#### Overview

These values can be set (initialized) exactly once, but read many times.

## Topics

### Initializers
- [init()](atomiclazyreference/init.md)
### Instance Methods
- [func load() -> Instance?](atomiclazyreference/load.md)
  Atomically loads and returns the current value of this reference.
- [func storeIfNil(consuming Instance) -> Instance](atomiclazyreference/storeifnil(_:).md)
  Atomically initializes this reference if its current value is nil, then returns the initialized value. If this reference is already initialized, then `storeIfNil(_:)` discards its supplied argument and returns the current value without updating it.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Atomic](atomic.md)
  An atomic value.
- [struct WordPair](wordpair.md)
  A pair of two word sized `UInt`s.
- [protocol AtomicRepresentable](atomicrepresentable.md)
  A type that supports atomic operations through a separate atomic storage representation.
- [protocol AtomicOptionalRepresentable](atomicoptionalrepresentable.md)
  An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomiclazyreference)*