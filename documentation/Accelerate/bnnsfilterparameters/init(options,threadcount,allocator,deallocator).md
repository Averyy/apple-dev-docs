# init(options:threadCount:allocator:deallocator:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new common filter parameters structure using the specified options.

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
init(options: BNNSFlags, threadCount: Int, allocator: BNNSAlloc?, deallocator: BNNSFree?)
```

## Parameters

- `options`: The options that control the behavior of a filter parameter.
- `threadCount`: The maximum number of threads that the filter executes. Set to `0` to specify that the filter automatically selects the number of threads. Set to `1` to specify that the filter operates on a single thread.
- `allocator`: The function the filter calls to allocate memory.
- `deallocator`: The function the filter calls to deallocate memory.

## See Also

### Initializers
- [init(flags: UInt32, n_threads: Int, alloc_memory: BNNSAlloc?, free_memory: BNNSFree?)](./init%28flags,n_threads,alloc_memory,free_memory%29.md)
  Returns a new common filter parameters structure.
- [init()](./init%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/init(options:threadcount:allocator:deallocator:))*