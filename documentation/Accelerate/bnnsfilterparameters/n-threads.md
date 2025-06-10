# n_threads

**Framework**: Accelerate  
**Kind**: property

The number of worker threads to execute.

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
var n_threads: Int
```

#### Discussion

If `0`, BNNS uses the best number of threads for the current machine.

## See Also

- [var flags: UInt32](bnnsfilterparameters/flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var alloc_memory: BNNSAlloc?](bnnsfilterparameters/alloc_memory.md)
  The function called to allocate memory.
- [var free_memory: BNNSFree?](bnnsfilterparameters/free_memory.md)
  The function called to deallocate memory.
- [var allocator: BNNSAlloc?](bnnsfilterparameters/allocator.md)
- [var deallocator: BNNSFree?](bnnsfilterparameters/deallocator.md)
- [var options: BNNSFlags](bnnsfilterparameters/options.md)
- [var threadCount: Int](bnnsfilterparameters/threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/n_threads)*