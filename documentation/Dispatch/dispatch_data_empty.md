# dispatch_data_empty

**Framework**: Dispatch  
**Kind**: macro  
**Role**: Macro

A dispatch data object representing a zero-length memory region.

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
#define dispatch_data_empty
```

## See Also

### Creating a Dispatch Data Object
- [dispatch_data_create](./dispatch_data_create.md)
  Creates a new dispatch data object with the specified memory buffer.
- [dispatch_data_create_map](./dispatch_data_create_map.md)
  Returns a new dispatch data object containing a contiguous representation of the specified object’s memory.
- [dispatch_data_create_concat](./dispatch_data_create_concat.md)
  Returns a new dispatch data object consisting of the concatenated data from two other data objects.
- [dispatch_data_create_subrange](./dispatch_data_create_subrange.md)
  Returns a new dispatch data object whose contents consist of a portion of another object’s memory region.
- [dispatch_data_copy_region](./dispatch_data_copy_region.md)
  Returns a data object containing a portion of the data in another data object.
- [typealias dispatch_data_t](./dispatch_data_t.md)
  An immutable object representing a contiguous or sparse region of memory.
- [OS_dispatch_data](./os_dispatch_data.md)
- [DISPATCH_DATA_DESTRUCTOR_DEFAULT](./dispatch_data_destructor_default.md)
  The default data destructor for dispatch objects.
- [DISPATCH_DATA_DESTRUCTOR_FREE](./dispatch_data_destructor_free.md)
  The destructor for dispatch data objects whose memory buffer was created using the malloc family of allocation routines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_empty)*