# free_memory

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The function called to deallocate memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var free_memory: BNNSFree?
```

```c
BNNSFree free_memory;
```

## Discussion

Must be compatible with the [`alloc_memory`](./alloc_memory.md) function. If `nil`, `free()` will be called.

## See Also

### Instance Properties
- [var flags: UInt32](./flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var n_threads: Int](./n_threads.md)
  The number of worker threads to execute.
- [var alloc_memory: BNNSAlloc?](./alloc_memory.md)
  The function called to allocate memory.
- [var allocator: BNNSAlloc?](./allocator.md)
- [var deallocator: BNNSFree?](./deallocator.md)
- [var options: BNNSFlags](./options.md)
- [var threadCount: Int](./threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/free_memory)*