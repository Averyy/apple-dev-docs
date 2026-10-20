# fdtype

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The file descriptor type, as a libproc type.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var fdtype: UInt32
```

```c
uint32_t fdtype;
```

#### Discussion

If this value is `PROX_FDTYPE_PIPE`, the [`es_fd_t`](../es_fd_t.md) structure also contains a `pipe.pipe_id` field. This field represents the unique ID of the pipe for correlation with other file descriptors pointing to the same or other end of the same pipe.

## See Also

### Inspecting File Descriptor Properties
- [var fd: Int32](./fd.md)
  The file descriptor number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_fd_t/fdtype)*