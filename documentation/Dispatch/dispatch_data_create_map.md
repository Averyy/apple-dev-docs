# dispatch_data_create_map

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns a new dispatch data object containing a contiguous representation of the specified object’s memory.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern dispatch_data_tdispatch_data_create_map(dispatch_data_t data, const void **buffer_ptr, size_t *size_ptr);
```

## Return Value

A new dispatch data object containing the contiguous version of the memory managed by the object in the `data` parameter.

## Discussion

If you specify non-`NULL` values for `buffer_ptr` or `size_ptr`, the values returned in those variables are valid only until you release the newly created dispatch data object. You can use these values as a quick way to access the data of the new data object.

## Parameters

- `data`: A dispatch data object containing the memory to map. If the object contains multiple noncontiguous memory regions, those regions are copied to a single, contiguous memory region for the new object.
- `buffer_ptr`: On input, a pointer to a variable in which to store the pointer to the memory region for the newly created dispatch data object. You may specify `NULL` for this parameter if you do not need the information.
- `size_ptr`: On input, a pointer to a variable in which to store the size of the contiguous memory region in the newly created dispatch data object. You may specify `NULL` for this parameter if you do not need the information.

## See Also

### Creating a Dispatch Data Object
- [dispatch_data_create](./dispatch_data_create.md)
  Creates a new dispatch data object with the specified memory buffer.
- [dispatch_data_create_concat](./dispatch_data_create_concat.md)
  Returns a new dispatch data object consisting of the concatenated data from two other data objects.
- [dispatch_data_create_subrange](./dispatch_data_create_subrange.md)
  Returns a new dispatch data object whose contents consist of a portion of another object’s memory region.
- [dispatch_data_copy_region](./dispatch_data_copy_region.md)
  Returns a data object containing a portion of the data in another data object.
- [dispatch_data_empty](./dispatch_data_empty.md)
  A dispatch data object representing a zero-length memory region.
- [typealias dispatch_data_t](./dispatch_data_t.md)
  An immutable object representing a contiguous or sparse region of memory.
- [OS_dispatch_data](./os_dispatch_data.md)
- [DISPATCH_DATA_DESTRUCTOR_DEFAULT](./dispatch_data_destructor_default.md)
  The default data destructor for dispatch objects.
- [DISPATCH_DATA_DESTRUCTOR_FREE](./dispatch_data_destructor_free.md)
  The destructor for dispatch data objects whose memory buffer was created using the malloc family of allocation routines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_create_map)*