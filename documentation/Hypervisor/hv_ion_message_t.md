# hv_ion_message_t

**Framework**: Hypervisor  
**Kind**: struct  
**Role**: Structure

The structure that describes the Mach message that the Hypervisor sends when an I/O notifier delivers the notifications you request.

**Availability**:
- macOS

## Declaration

```swift
struct hv_ion_message_t
```

```c
typedef struct { ... } hv_ion_message_t;
```

## Topics

### Initializers
- [init()](./hv_ion_message_t/init%28%29.md)
  Creates a new I/O notifier message.
- [init(header: mach_msg_header_t, addr: UInt64, size: UInt64, value: UInt64, trailer: mach_msg_trailer_t)](./hv_ion_message_t/init%28header,addr,size,value,trailer%29.md)
  Creates a new I/O notifier message with the parameters you provide.
### Instance properties
- [var addr: UInt64](./hv_ion_message_t/addr.md)
  The address of the I/O write.
- [var header: mach_msg_header_t](./hv_ion_message_t/header.md)
  The Mach message header.
- [var size: UInt64](./hv_ion_message_t/size.md)
  The size of the value written by the notifier.
- [var trailer: mach_msg_trailer_t](./hv_ion_message_t/trailer.md)
  The Mach message trailer.
- [var value: UInt64](./hv_ion_message_t/value.md)
  An unsigned 64-bit integer that represents the contents of an I/O notifier message.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### I/O notifier functions
- [func hv_vm_add_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](./hv_vm_add_pio_notifier%28_,_,_,_,_%29.md)
  Generate a notification when the Hypervisor issues a matching guest port I/O.
- [func hv_vm_remove_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](./hv_vm_remove_pio_notifier%28_,_,_,_,_%29.md)
  Removes an existing I/O notifier that matches the specifications you provide.
- [typealias hv_ion_flags_t](./hv_ion_flags_t.md)
  The bitfield that you use to set the options flags for the I/O notifier.
- [I/O Notifier Flags](./api-3727903-i-o-notifier-flags.md)
  Flags that you set to choose the kind of information the I/O Notifier delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_message_t)*