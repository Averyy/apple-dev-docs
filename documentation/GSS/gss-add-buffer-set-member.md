# gss_add_buffer_set_member(_:_:_:)

**Framework**: GSS  
**Kind**: func

Copies the contents of a buffer into a buffer set.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_add_buffer_set_member(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ member_buffer: gss_buffer_t, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success, or [`GSS_S_FAILURE`](gss_s_failure.md) otherwise. Inspect the `minor_status` parameter for additional information on failure.

#### Discussion

The function does not add the `member_buffer` to the buffer set directly. Rather it allocates new memory for a copy of the buffer, which it includes in the buffer set. When you call [`gss_release_buffer_set(_:_:)`](gss_release_buffer_set(_:_:).md) later, you deallocate the memory for the buffer set and all of its buffer copies, but this has no effect on the original `member_buffer`.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure. Typically, a failure results from an inability to allocate memory, communicated with minor status  .
- `member_buffer`: The buffer to copy into the buffer set.
- `buffer_set`: A pointer to a buffer set descriptor reference that receives a copy of the buffer. You can indicate that the buffer set doesn’t yet exist by setting its reference to  . In this case, the function creates it first using  . In any case, the buffer is added to the end of the set, and the buffer set’s   parameter incremented.

## See Also

- [func gss_create_empty_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_create_empty_buffer_set(_:_:).md)
  Allocates an empty buffer set descriptor that you use to manage an array of buffers.
- [func gss_release_buffer(UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](gss_release_buffer(_:_:).md)
  Frees the memory associated with a single buffer descriptor.
- [func gss_release_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_release_buffer_set(_:_:).md)
  Frees the memory associated with a buffer set descriptor and all the buffers it contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_add_buffer_set_member(_:_:_:))*