# options

**Framework**: Accelerate  
**Kind**: property

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var options: BNNSFlags { get set }
```

## See Also

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
- [var threadCount: Int](bnnsfilterparameters/threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/options)*