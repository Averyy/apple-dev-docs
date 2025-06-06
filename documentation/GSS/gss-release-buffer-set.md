# gss_release_buffer_set(_:_:)

**Framework**: GSS  
**Kind**: func

Frees the memory associated with a buffer set descriptor and all the buffers it contains.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_release_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32
```

## Mentions

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on completion.

#### Discussion

This call frees the memory of all of the buffers that the buffer set contains, as well as the buffer set descriptor itself. Use this function when you’re done with a buffer set that you created with [`gss_create_empty_buffer_set(_:_:)`](gss_create_empty_buffer_set(_:_:).md), or created on your behalf by [`gss_add_buffer_set_member(_:_:_:)`](gss_add_buffer_set_member(_:_:_:).md).

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `buffer_set`: A pointer to the buffer set descriptor reference that you want to free.

## See Also

- [func gss_create_empty_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_create_empty_buffer_set(_:_:).md)
  Allocates an empty buffer set descriptor that you use to manage an array of buffers.
- [func gss_add_buffer_set_member(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32](gss_add_buffer_set_member(_:_:_:).md)
  Copies the contents of a buffer into a buffer set.
- [func gss_release_buffer(UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](gss_release_buffer(_:_:).md)
  Frees the memory associated with a single buffer descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_release_buffer_set(_:_:))*