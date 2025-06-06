# AtomicUpdateOrdering

**Framework**: Synchronization  
**Kind**: struct

Specifies the memory ordering semantics of an atomic read-modify-write operation.

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
struct AtomicUpdateOrdering
```

## Topics

### Type Properties
- [static var acquiring: AtomicUpdateOrdering](atomicupdateordering/acquiring.md)
  An acquiring update synchronizes with a releasing operation whose value its reads. It ensures that the releasing and acquiring threads agree that all subsequent variable accesses on the acquiring thread happen after the atomic operation itself.
- [static var acquiringAndReleasing: AtomicUpdateOrdering](atomicupdateordering/acquiringandreleasing.md)
  An acquiring-and-releasing operation is a combination of `.acquiring` and `.releasing` operation on the same variable.
- [static var relaxed: AtomicUpdateOrdering](atomicupdateordering/relaxed.md)
  Guarantees the atomicity of the specific operation on which it is applied, but imposes no ordering constraints on any other variable accesses.
- [static var releasing: AtomicUpdateOrdering](atomicupdateordering/releasing.md)
  A releasing update synchronizes with acquiring operations that read the value it stores. It ensures that the releasing and acquiring threads agree that all preceding variable accesses on the releasing thread happen before the atomic operation itself.
- [static var sequentiallyConsistent: AtomicUpdateOrdering](atomicupdateordering/sequentiallyconsistent.md)
  A sequentially consistent update performs an acquiring-and-releasing update and also guarantees that it and all other sequentially consistent atomic operations (loads, stores, updates) appear to be executed in a single, total sequential ordering.
### Default Implementations
- [CustomStringConvertible Implementations](atomicupdateordering/customstringconvertible-implementations.md)
- [Equatable Implementations](atomicupdateordering/equatable-implementations.md)
- [Hashable Implementations](atomicupdateordering/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct AtomicLoadOrdering](atomicloadordering.md)
  Specifies the memory ordering semantics of an atomic load operation.
- [struct AtomicStoreOrdering](atomicstoreordering.md)
  Specifies the memory ordering semantics of an atomic store operation.
- [func atomicMemoryFence(ordering: AtomicUpdateOrdering)](atomicmemoryfence(ordering:).md)
  Establishes a memory ordering without associating it with a particular atomic operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicupdateordering)*