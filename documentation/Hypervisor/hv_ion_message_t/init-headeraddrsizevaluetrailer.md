# init(header:addr:size:value:trailer:)

**Framework**: Hypervisor  
**Kind**: init

Creates a new I/O notifier message with the parameters you provide.

**Availability**:
- macOS ?+

## Declaration

```swift
init(header: mach_msg_header_t, addr: UInt64, size: UInt64, value: UInt64, trailer: mach_msg_trailer_t)
```

## Parameters

- `header`: The Mach message header.
- `addr`: The address of the I/O write.
- `size`: The size of the value written.
- `value`: The value written to  .
- `trailer`: The Mach message trailer.

## See Also

- [init()](hv_ion_message_t/init.md)
  Creates a new I/O notifier message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_message_t/init(header:addr:size:value:trailer:))*