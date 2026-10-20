# addr

**Framework**: Hypervisor  
**Kind**: property  
**Role**: Instance Property

The address of the I/O write.

**Availability**:
- macOS

## Declaration

```swift
var addr: UInt64
```

```c
uint64_t addr;
```

## See Also

### Instance properties
- [var header: mach_msg_header_t](./header.md)
  The Mach message header.
- [var size: UInt64](./size.md)
  The size of the value written by the notifier.
- [var trailer: mach_msg_trailer_t](./trailer.md)
  The Mach message trailer.
- [var value: UInt64](./value.md)
  An unsigned 64-bit integer that represents the contents of an I/O notifier message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_message_t/addr)*