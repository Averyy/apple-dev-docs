# init(flags:n_threads:alloc_memory:free_memory:)

**Framework**: Accelerate  
**Kind**: init

Returns a new common filter parameters structure.

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
init(flags: UInt32, n_threads: Int, alloc_memory: BNNSAlloc?, free_memory: BNNSFree?)
```

#### Return Value

A new common filter parameters structure.

#### Discussion

If `alloc_memory` is null, BNNS uses `posix_memalign(_:_:_:)` for memory allocation. If free_memory is null, BNNS uses `free()` for memory deallocation.

## Parameters

- `flags`: A logical OR of zero or more values from BNNS flags.
- `n_threads`: The maximum number of threads that the filter executes. Set to   to specify that the filter automatically selects the number of threads. Set to   to specify that the filter operates on a single thread.
- `alloc_memory`: The function the filter calls to allocate memory.
- `free_memory`: The function the filter calls to deallocate memory.

## See Also

- [init(options: BNNSFlags, threadCount: Int, allocator: BNNSAlloc?, deallocator: BNNSFree?)](bnnsfilterparameters/init(options:threadcount:allocator:deallocator:).md)
  Returns a new common filter parameters structure using the specified options.
- [init()](bnnsfilterparameters/init.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters/init(flags:n_threads:alloc_memory:free_memory:))*