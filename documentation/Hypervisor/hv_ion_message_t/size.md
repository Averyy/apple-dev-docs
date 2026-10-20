# size

**Framework**: Hypervisor  
**Kind**: property  
**Role**: Instance Property

The size of the value written by the notifier.

**Availability**:
- macOS

## Declaration

```swift
var size: UInt64
```

```c
uint64_t size;
```

## See Also

### Instance properties
- [var addr: UInt64](./addr.md)
  The address of the I/O write.
- [var header: mach_msg_header_t](./header.md)
  The Mach message header.
- [var trailer: mach_msg_trailer_t](./trailer.md)
  The Mach message trailer.
- [var value: UInt64](./value.md)
  An unsigned 64-bit integer that represents the contents of an I/O notifier message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_message_t/size)*