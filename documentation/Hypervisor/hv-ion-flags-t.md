# hv_ion_flags_t

**Framework**: Hypervisor  
**Kind**: typealias

The bitfield that you use to set the options flags for the I/O notifier.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_ion_flags_t = UInt32
```

## See Also

- [func hv_vm_add_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](hv_vm_add_pio_notifier(_:_:_:_:_:).md)
  Generate a notification when the Hypervisor issues a matching guest port I/O.
- [func hv_vm_remove_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](hv_vm_remove_pio_notifier(_:_:_:_:_:).md)
  Removes an existing I/O notifier that matches the specifications you provide.
- [struct hv_ion_message_t](hv_ion_message_t.md)
  The structure that describes the Mach message that the Hypervisor sends when an I/O notifier delivers the notifications you request.
- [I/O Notifier Flags](3727903-i-o-notifier-flags.md)
  Flags that you set to choose the kind of information the I/O Notifier delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_flags_t)*