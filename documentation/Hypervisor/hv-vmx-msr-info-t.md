# hv_vmx_msr_info_t

**Framework**: Hypervisor  
**Kind**: typealias

The type that describes Move to Status Register (MSR) information fields.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vmx_msr_info_t = UInt64
```

## See Also

- [func hv_vmx_read_capability(hv_vmx_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_read_capability(_:_:).md)
  Returns, by reference, the VMX virtualization capabilities of the host processor.
- [func hv_vmx_get_msr_info(hv_vmx_msr_info_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_get_msr_info(_:_:).md)
  Returns information about guest MSR configuration.
- [struct hv_vmx_capability_t](hv_vmx_capability_t.md)
  The type that describes Virtual Machine Extensions (VMX) capability fields.
- [VMX Capabilities](1469645-vmx-capabilities.md)
  An enumeration that represents the available VMX capabilities.
- [MSR Information Fields](3567084-msr-information-fields.md)
  The type that describes Machine Specific Register (MSR) fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vmx_msr_info_t)*