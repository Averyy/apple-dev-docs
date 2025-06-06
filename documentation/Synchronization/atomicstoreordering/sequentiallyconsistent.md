# sequentiallyConsistent

**Framework**: Synchronization  
**Kind**: property

A sequentially consistent store performs a releasing store and also guarantees that it and all other sequentially consistent atomic operations (loads, stores, updates) appear to be executed in a single, total sequential ordering.

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
static var sequentiallyConsistent: AtomicStoreOrdering { get }
```

#### Discussion

This value corresponds to `std::memory_order_seq_cst` in C++.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicstoreordering/sequentiallyconsistent)*