# flags

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A logical OR of zero or more values from BNNS flags.

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
var flags: UInt32
```

```c
uint32_t flags;
```

## See Also

### Instance Properties
- [var n_threads: Int](./n_threads.md)
  The number of worker threads to execute.
- [var alloc_memory: BNNSAlloc?](./alloc_memory.md)
  The function called to allocate memory.
- [var free_memory: BNNSFree?](./free_memory.md)
  The function called to deallocate memory.
- [var allocator: BNNSAlloc?](./allocator.md)
- [var deallocator: BNNSFree?](./deallocator.md)
- [var options: BNNSFlags](./options.md)
- [var threadCount: Int](./threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/flags)*