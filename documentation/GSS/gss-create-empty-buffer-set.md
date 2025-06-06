# gss_create_empty_buffer_set(_:_:)

**Framework**: GSS  
**Kind**: func

Allocates an empty buffer set descriptor that you use to manage an array of buffers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_create_empty_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32
```

## Mentions

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success, or [`GSS_S_FAILURE`](gss_s_failure.md) otherwise. Inspect the `minor_status` parameter for additional information on failure.

#### Discussion

This function allocates memory for the data structure that you use to manage an array of buffers, consisting of a length parameter and a pointer. It does not allocate memory for any actual buffers.

When you’re done with the buffer set descriptor created by this function, call [`gss_release_buffer_set(_:_:)`](gss_release_buffer_set(_:_:).md) to free its memory, as well as that of any buffers it contains at that time.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure. Typically, a failure results from an inability to allocate memory which is communicated by the minor status  .
- `buffer_set`: On failure, the reference is unchanged.

## See Also

- [func gss_add_buffer_set_member(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32](gss_add_buffer_set_member(_:_:_:).md)
  Copies the contents of a buffer into a buffer set.
- [func gss_release_buffer(UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](gss_release_buffer(_:_:).md)
  Frees the memory associated with a single buffer descriptor.
- [func gss_release_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_release_buffer_set(_:_:).md)
  Frees the memory associated with a buffer set descriptor and all the buffers it contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_create_empty_buffer_set(_:_:))*