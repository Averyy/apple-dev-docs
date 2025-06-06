# hv_vm_remove_pio_notifier(_:_:_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Removes an existing I/O notifier that matches the specifications you provide.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vm_remove_pio_notifier(_ addr: UInt16, _ size: Int, _ value: UInt32, _ mach_port: mach_port_t, _ flags: hv_ion_flags_t) -> hv_return_t
```

#### Return Value

`0` on success, or an [`hv_return_t`](hv_return_t.md) error code.

#### Discussion

The arguments you provide must match those previously used to add the notifier.

## Parameters

- `addr`: The port I/O address of the existing notifier.
- `size`: The match-size from the existing notifier.
- `value`: The value to match against from the existing notifier.
- `mach_port`: The Mach port from the existing notifier.
- `flags`: The   option flags from the existing notifier.

## See Also

- [func hv_vm_add_pio_notifier(UInt16, Int, UInt32, mach_port_t, hv_ion_flags_t) -> hv_return_t](hv_vm_add_pio_notifier(_:_:_:_:_:).md)
  Generate a notification when the Hypervisor issues a matching guest port I/O.
- [struct hv_ion_message_t](hv_ion_message_t.md)
  The structure that describes the Mach message that the Hypervisor sends when an I/O notifier delivers the notifications you request.
- [typealias hv_ion_flags_t](hv_ion_flags_t.md)
  The bitfield that you use to set the options flags for the I/O notifier.
- [I/O Notifier Flags](3727903-i-o-notifier-flags.md)
  Flags that you set to choose the kind of information the I/O Notifier delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_remove_pio_notifier(_:_:_:_:_:))*