# I/O Notifier Flags

**Framework**: Hypervisor

Flags that you set to choose the kind of information the I/O Notifier delivers.

## Topics

### Notifier options
- [var HV_ION_ANY_SIZE: Int](hv_ion_any_size.md)
  The value that represents a request for notifications of an I/O result of any size.
- [var HV_ION_ANY_VALUE: Int](hv_ion_any_value.md)
  The value that represents a request for notifications of an I/O result that contains any value.
- [var HV_ION_EXIT_FULL: Int](hv_ion_exit_full.md)
  The value that represents a request for notifications if the I/O queue is full.
- [var HV_ION_NONE: Int](hv_ion_none.md)
  The value that represents a request for no notifications.

## See Also

- [func hv_vm_add_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](hv_vm_add_pio_notifier(_:_:_:_:_:).md)
  Generate a notification when the Hypervisor issues a matching guest port I/O.
- [func hv_vm_remove_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](hv_vm_remove_pio_notifier(_:_:_:_:_:).md)
  Removes an existing I/O notifier that matches the specifications you provide.
- [struct hv_ion_message_t](hv_ion_message_t.md)
  The structure that describes the Mach message that the Hypervisor sends when an I/O notifier delivers the notifications you request.
- [typealias hv_ion_flags_t](hv_ion_flags_t.md)
  The bitfield that you use to set the options flags for the I/O notifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/3727903-i-o-notifier-flags)*