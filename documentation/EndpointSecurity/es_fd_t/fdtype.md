# fdtype

**Framework**: Endpoint Security  
**Kind**: property

The file descriptor type, as a libproc type.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var fdtype: UInt32
```

#### Discussion

If this value is `PROX_FDTYPE_PIPE`, the [`es_fd_t`](es_fd_t.md) structure also contains a `pipe.pipe_id` field. This field represents the unique ID of the pipe for correlation with other file descriptors pointing to the same or other end of the same pipe.

## See Also

- [var fd: Int32](es_fd_t/fd.md)
  The file descriptor number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_fd_t/fdtype)*