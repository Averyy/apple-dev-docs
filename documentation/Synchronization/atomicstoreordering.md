# AtomicStoreOrdering

**Framework**: Synchronization  
**Kind**: struct

Specifies the memory ordering semantics of an atomic store operation.

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
struct AtomicStoreOrdering
```

## Topics

### Type Properties
- [static var relaxed: AtomicStoreOrdering](atomicstoreordering/relaxed.md)
  Guarantees the atomicity of the specific operation on which it is applied, but imposes no ordering constraints on any other variable accesses.
- [static var releasing: AtomicStoreOrdering](atomicstoreordering/releasing.md)
  A releasing store synchronizes with acquiring operations that read the value it stores. It ensures that the releasing and acquiring threads agree that all preceding variable accesses on the releasing thread happen before the atomic operation itself.
- [static var sequentiallyConsistent: AtomicStoreOrdering](atomicstoreordering/sequentiallyconsistent.md)
  A sequentially consistent store performs a releasing store and also guarantees that it and all other sequentially consistent atomic operations (loads, stores, updates) appear to be executed in a single, total sequential ordering.
### Default Implementations
- [CustomStringConvertible Implementations](atomicstoreordering/customstringconvertible-implementations.md)
- [Equatable Implementations](atomicstoreordering/equatable-implementations.md)
- [Hashable Implementations](atomicstoreordering/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AtomicLoadOrdering](atomicloadordering.md)
  Specifies the memory ordering semantics of an atomic load operation.
- [struct AtomicUpdateOrdering](atomicupdateordering.md)
  Specifies the memory ordering semantics of an atomic read-modify-write operation.
- [func atomicMemoryFence(ordering: AtomicUpdateOrdering)](atomicmemoryfence(ordering:).md)
  Establishes a memory ordering without associating it with a particular atomic operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicstoreordering)*