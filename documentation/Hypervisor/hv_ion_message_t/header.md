# header

**Framework**: Hypervisor  
**Kind**: property  
**Role**: Instance Property

The Mach message header.

**Availability**:
- macOS

## Declaration

```swift
var header: mach_msg_header_t
```

```c
mach_msg_header_t header;
```

## See Also

### Instance properties
- [var addr: UInt64](./addr.md)
  The address of the I/O write.
- [var size: UInt64](./size.md)
  The size of the value written by the notifier.
- [var trailer: mach_msg_trailer_t](./trailer.md)
  The Mach message trailer.
- [var value: UInt64](./value.md)
  An unsigned 64-bit integer that represents the contents of an I/O notifier message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_message_t/header)*