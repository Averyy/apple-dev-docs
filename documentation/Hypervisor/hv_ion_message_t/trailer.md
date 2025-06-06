# trailer

**Framework**: Hypervisor  
**Kind**: property

The Mach message trailer.

**Availability**:
- macOS ?+

## Declaration

```swift
var trailer: mach_msg_trailer_t
```

## See Also

- [var addr: UInt64](hv_ion_message_t/addr.md)
  The address of the I/O write.
- [var header: mach_msg_header_t](hv_ion_message_t/header.md)
  The Mach message header.
- [var size: UInt64](hv_ion_message_t/size.md)
  The size of the value written by the notifier.
- [var value: UInt64](hv_ion_message_t/value.md)
  An unsigned 64-bit integer that represents the contents of an I/O notifier message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_message_t/trailer)*