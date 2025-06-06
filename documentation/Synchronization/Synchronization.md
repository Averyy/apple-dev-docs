# Synchronization

**Framework**: Synchronization  
**Kind**: module

Build synchronization constructs using low-level, primitive operations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Topics

### Atomic Values
- [struct Atomic](atomic.md)
  An atomic value.
- [struct AtomicLazyReference](atomiclazyreference.md)
  A lazily initializable atomic strong reference.
- [struct WordPair](wordpair.md)
  A pair of two word sized `UInt`s.
- [protocol AtomicRepresentable](atomicrepresentable.md)
  A type that supports atomic operations through a separate atomic storage representation.
- [protocol AtomicOptionalRepresentable](atomicoptionalrepresentable.md)
  An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.
### Memory Ordering Semantics
- [struct AtomicLoadOrdering](atomicloadordering.md)
  Specifies the memory ordering semantics of an atomic load operation.
- [struct AtomicStoreOrdering](atomicstoreordering.md)
  Specifies the memory ordering semantics of an atomic store operation.
- [struct AtomicUpdateOrdering](atomicupdateordering.md)
  Specifies the memory ordering semantics of an atomic read-modify-write operation.
- [func atomicMemoryFence(ordering: AtomicUpdateOrdering)](atomicmemoryfence(ordering:).md)
  Establishes a memory ordering without associating it with a particular atomic operation.
### Structures
- [struct Mutex](mutex.md)
  A synchronization primitive that protects shared mutable state via mutual exclusion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Synchronization)*