# dispatch_data_applier_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

A block to invoke for every contiguous memory region in a data object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef _Bool (^)(NSObject<OS_dispatch_data> *, unsigned long, const void *, unsigned long) dispatch_data_applier_t;
```

## Discussion

The parameters of a dispatch data applier block are as follows:

- `region` - A data object containing the current memory region being analyzed.
- `offset` - The logical offset to the current region from the start of the data object.
- `buffer` - A pointer to the memory for the current region.
- `size` - The size of the memory for the current region.

This handler returns a Boolean value indicating whether traversal of the region should continue.

## See Also

### Applying Changes to the Data
- [dispatch_data_apply](./dispatch_data_apply.md)
  Traverses the memory of a dispatch data object and executes custom code on each region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_applier_t)*