# BNNSFilterParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains common filter parameters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSFilterParameters
```

## Topics

### Initializers
- [init(options: BNNSFlags, threadCount: Int, allocator: BNNSAlloc?, deallocator: BNNSFree?)](bnnsfilterparameters/init(options:threadcount:allocator:deallocator:).md)
  Returns a new common filter parameters structure using the specified options.
- [init(flags: UInt32, n_threads: Int, alloc_memory: BNNSAlloc?, free_memory: BNNSFree?)](bnnsfilterparameters/init(flags:n_threads:alloc_memory:free_memory:).md)
  Returns a new common filter parameters structure.
- [init()](bnnsfilterparameters/init.md)
### Instance Properties
- [var flags: UInt32](bnnsfilterparameters/flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var n_threads: Int](bnnsfilterparameters/n_threads.md)
  The number of worker threads to execute.
- [var alloc_memory: BNNSAlloc?](bnnsfilterparameters/alloc_memory.md)
  The function called to allocate memory.
- [var free_memory: BNNSFree?](bnnsfilterparameters/free_memory.md)
  The function called to deallocate memory.
- [var allocator: BNNSAlloc?](bnnsfilterparameters/allocator.md)
- [var deallocator: BNNSFree?](bnnsfilterparameters/deallocator.md)
- [var options: BNNSFlags](bnnsfilterparameters/options.md)
- [var threadCount: Int](bnnsfilterparameters/threadcount.md)
### Filter Flags
- [struct BNNSFlags](bnnsflags.md)
  Options that control the behavior of a filter parameter.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias BNNSFilter](bnnsfilter.md)
  An opaque type that represents a filter.
- [Applying Filters](applying-filters.md)
- [class Layer](bnns/layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class UnaryLayer](bnns/unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](bnns/binarylayer.md)
  The base class for layers that accept two inputs.
- [func BNNSFilterDestroy(BNNSFilter?)](bnnsfilterdestroy(_:).md)
  Destroys the specified filter, releasing all resources allocated for it.
- [typealias BNNSAlloc](bnnsalloc.md)
  A type-alias for a user-provided memory allocation function.
- [typealias BNNSFree](bnnsfree.md)
  A type-alias for a user-provided memory deallocation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters)*