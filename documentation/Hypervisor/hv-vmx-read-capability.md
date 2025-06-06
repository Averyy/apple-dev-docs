# hv_vmx_read_capability(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns, by reference, the VMX virtualization capabilities of the host processor.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vmx_read_capability(_ field: hv_vmx_capability_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

 This function must be called by the owning thread.

## Parameters

- `field`: The capability of the host processor to return. For a list of field IDs, see  .
- `value`: The value of the capability  , on output. For a list of possible values, see  .

## See Also

- [func hv_vmx_get_msr_info(hv_vmx_msr_info_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_get_msr_info(_:_:).md)
  Returns information about guest MSR configuration.
- [struct hv_vmx_capability_t](hv_vmx_capability_t.md)
  The type that describes Virtual Machine Extensions (VMX) capability fields.
- [VMX Capabilities](1469645-vmx-capabilities.md)
  An enumeration that represents the available VMX capabilities.
- [typealias hv_vmx_msr_info_t](hv_vmx_msr_info_t.md)
  The type that describes Move to Status Register (MSR) information fields.
- [MSR Information Fields](3567084-msr-information-fields.md)
  The type that describes Machine Specific Register (MSR) fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vmx_read_capability(_:_:))*