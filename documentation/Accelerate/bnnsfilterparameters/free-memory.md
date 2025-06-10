# free_memory

**Framework**: Accelerate  
**Kind**: property

The function called to deallocate memory.

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
var free_memory: BNNSFree?
```

#### Discussion

Must be compatible with the [`alloc_memory`](bnnsfilterparameters/alloc_memory.md) function. If `nil`, `free()` will be called.

## See Also

- [var flags: UInt32](bnnsfilterparameters/flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var n_threads: Int](bnnsfilterparameters/n_threads.md)
  The number of worker threads to execute.
- [var alloc_memory: BNNSAlloc?](bnnsfilterparameters/alloc_memory.md)
  The function called to allocate memory.
- [var allocator: BNNSAlloc?](bnnsfilterparameters/allocator.md)
- [var deallocator: BNNSFree?](bnnsfilterparameters/deallocator.md)
- [var options: BNNSFlags](bnnsfilterparameters/options.md)
- [var threadCount: Int](bnnsfilterparameters/threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/free_memory)*