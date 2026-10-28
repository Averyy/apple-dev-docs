# n_threads

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of worker threads to execute.

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
var n_threads: Int
```

```c
size_t n_threads;
```

## Discussion

If `0`, BNNS uses the best number of threads for the current machine.

## See Also

### Instance Properties
- [var flags: UInt32](./flags.md)
  A logical OR of zero or more values from BNNS flags.
- [var alloc_memory: BNNSAlloc?](./alloc_memory.md)
  The function called to allocate memory.
- [var free_memory: BNNSFree?](./free_memory.md)
  The function called to deallocate memory.
- [var allocator: BNNSAlloc?](./allocator.md)
- [var deallocator: BNNSFree?](./deallocator.md)
- [var options: BNNSFlags](./options.md)
- [var threadCount: Int](./threadcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/n_threads)*