# alloc_memory

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The function called to allocate memory.

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
var alloc_memory: BNNSAlloc?
```

```c
BNNSAlloc alloc_memory;
```

## Discussion

Must be compatible with the [`free_memory`](./free_memory.md) function. If `nil`, `posix_memalign(_:_:_:)` will be called.

## See Also

### Instance Properties
- [var flags: UInt32](./flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var n_threads: Int](./n_threads.md)
  The number of worker threads to execute.
- [var free_memory: BNNSFree?](./free_memory.md)
  The function called to deallocate memory.
- [var allocator: BNNSAlloc?](./allocator.md)
- [var deallocator: BNNSFree?](./deallocator.md)
- [var options: BNNSFlags](./options.md)
- [var threadCount: Int](./threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/alloc_memory)*