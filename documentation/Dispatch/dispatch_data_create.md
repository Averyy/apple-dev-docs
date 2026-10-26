# dispatch_data_create

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new dispatch data object with the specified memory buffer.

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
extern dispatch_data_tdispatch_data_create(const void *buffer, size_t size, dispatch_queue_t queue, dispatch_block_t destructor);
```

#### Return Value

A new data object containing the desired data. This object is retained initially. It is your responsibility to release the data object when you are done using it.

#### Discussion

If buffer is `NULL` or size is `0`, this function returns an empty dispatch object.

#### Discussion

If you specify the default destructor using the [`DISPATCH_DATA_DESTRUCTOR_DEFAULT`](./dispatch_data_destructor_default.md) constant, this function creates a copy of the data in `buffer` and manages that data internally. If you specify any other value, this function stores a pointer to your buffer and leaves the responsibility of releasing that buffer to the destructor you provide.

When you release the last reference to the object, the system typically enqueues the block in `destructor` on the provided queue. However, if you specify the [`DISPATCH_DATA_DESTRUCTOR_FREE`](./dispatch_data_destructor_free.md) constant for the destructor, the system simply frees the associated memory inline.

## Parameters

- `buffer`: A contiguous buffer of memory containing the desired data.
- `size`: The size of `buffer`, measured in bytes.
- `queue`: The queue on which to call `destructor` when it is time to release the data object. The queue is retained by the data object.
- `destructor`: The block responsible for releasing the memory associated with the data object. Specify [`DISPATCH_DATA_DESTRUCTOR_DEFAULT`](./dispatch_data_destructor_default.md) to use the default destructor for dispatch objects. Specify [`DISPATCH_DATA_DESTRUCTOR_FREE`](./dispatch_data_destructor_free.md) to use the destructor for malloc-based buffers.

## See Also

### Creating a Dispatch Data Object
- [dispatch_data_create_map](./dispatch_data_create_map.md)
  Returns a new dispatch data object containing a contiguous representation of the specified object’s memory.
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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_create)*