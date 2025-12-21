# AtomicLoadOrdering

**Framework**: Synchronization  
**Kind**: struct

Specifies the memory ordering semantics of an atomic load operation.

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
struct AtomicLoadOrdering
```

## Topics

### Type Properties
- [static var acquiring: AtomicLoadOrdering](atomicloadordering/acquiring.md)
  An acquiring load synchronizes with a releasing operation whose value its reads. It ensures that the releasing and acquiring threads agree that all subsequent variable accesses on the acquiring thread happen after the atomic operation itself.
- [static var relaxed: AtomicLoadOrdering](atomicloadordering/relaxed.md)
  Guarantees the atomicity of the specific operation on which it is applied, but imposes no ordering constraints on any other variable accesses.
- [static var sequentiallyConsistent: AtomicLoadOrdering](atomicloadordering/sequentiallyconsistent.md)
  A sequentially consistent load performs an acquiring load and also guarantees that it and all other sequentially consistent atomic operations (loads, stores, updates) appear to be executed in a single, total sequential ordering.

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

- [struct AtomicStoreOrdering](atomicstoreordering.md)
  Specifies the memory ordering semantics of an atomic store operation.
- [struct AtomicUpdateOrdering](atomicupdateordering.md)
  Specifies the memory ordering semantics of an atomic read-modify-write operation.
- [func atomicMemoryFence(ordering: AtomicUpdateOrdering)](atomicmemoryfence(ordering:).md)
  Establishes a memory ordering without associating it with a particular atomic operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicloadordering)*