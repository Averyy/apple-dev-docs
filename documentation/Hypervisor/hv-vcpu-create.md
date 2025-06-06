# hv_vcpu_create(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Creates a vCPU instance for the current thread.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_create(_ vcpu: UnsafeMutablePointer<hv_vcpu_t>, _ exit: UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, _ config: hv_vcpu_config_t?) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

Intel-based Mac computers have different parameters:

- `flags`: The vCPU creation flag. The available flags are [`HV_VCPU_ACCEL_RDPMC`](hv_vcpu_accel_rdpmc.md), [`HV_VCPU_TSC_RELATIVE`](hv_vcpu_tsc_relative.md), and [`HV_VCPU_DEFAULT`](hv_vcpu_default.md). The default is [`HV_VCPU_DEFAULT`](hv_vcpu_default.md).

> **Note**:  Using the [`HV_VCPU_TSC_RELATIVE`](hv_vcpu_tsc_relative.md) flag enables use of the Time-Stamp Counter (TSC) relative offset capabilities, but disables the default TSC for vCPUs that you create with this flag.

 Using the [`HV_VCPU_TSC_RELATIVE`](hv_vcpu_tsc_relative.md) flag enables use of the Time-Stamp Counter (TSC) relative offset capabilities, but disables the default TSC for vCPUs that you create with this flag.

## Parameters

- `vcpu`: An argument that the hypervisor populates with the instance of a vCPU on a successful return.
- `exit`: Apple silicon only.
- `config`: Apple silicon only.

## See Also

- [func hv_vm_get_max_vcpu_count(UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_get_max_vcpu_count(_:).md)
  Returns the maximum number of vCPUs that the hypervisor supports.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](hv_vcpu_destroy(_:).md)
  Destroys the vCPU instance associated with the current thread.
- [typealias hv_vcpu_t](hv_vcpu_t.md)
  An opaque value that represents a vCPU instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_create(_:_:_:))*