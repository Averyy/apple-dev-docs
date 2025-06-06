# hv_vmx_get_msr_info(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns information about guest MSR configuration.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vmx_get_msr_info(_ field: hv_vmx_msr_info_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

## Mentions

- [Extending vCPU Capabilities Using Model-Specific Registers](extending-vcpu-capabilities-using-model-specific-registers.md)

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

## Parameters

- `field`: The ID of the MSR to examine.
- `value`: A pointer to the info field value written by Hypervisor on a successful operation.

## See Also

- [func hv_vmx_read_capability(hv_vmx_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_read_capability(_:_:).md)
  Returns, by reference, the VMX virtualization capabilities of the host processor.
- [struct hv_vmx_capability_t](hv_vmx_capability_t.md)
  The type that describes Virtual Machine Extensions (VMX) capability fields.
- [VMX Capabilities](1469645-vmx-capabilities.md)
  An enumeration that represents the available VMX capabilities.
- [typealias hv_vmx_msr_info_t](hv_vmx_msr_info_t.md)
  The type that describes Move to Status Register (MSR) information fields.
- [MSR Information Fields](3567084-msr-information-fields.md)
  The type that describes Machine Specific Register (MSR) fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vmx_get_msr_info(_:_:))*