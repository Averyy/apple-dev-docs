# alloc_memory

**Framework**: Accelerate  
**Kind**: property

The function called to allocate memory.

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
var alloc_memory: BNNSAlloc?
```

#### Discussion

Must be compatible with the [`free_memory`](bnnsfilterparameters/free_memory.md) function. If `nil`, `posix_memalign(_:_:_:)` will be called.

## See Also

- [var flags: UInt32](bnnsfilterparameters/flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var n_threads: Int](bnnsfilterparameters/n_threads.md)
  The number of worker threads to execute.
- [var free_memory: BNNSFree?](bnnsfilterparameters/free_memory.md)
  The function called to deallocate memory.
- [var allocator: BNNSAlloc?](bnnsfilterparameters/allocator.md)
- [var deallocator: BNNSFree?](bnnsfilterparameters/deallocator.md)
- [var options: BNNSFlags](bnnsfilterparameters/options.md)
- [var threadCount: Int](bnnsfilterparameters/threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/alloc_memory)*