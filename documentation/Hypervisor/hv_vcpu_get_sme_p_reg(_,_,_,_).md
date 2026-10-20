# hv_vcpu_get_sme_p_reg(_:_:_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Returns the value of a vCPU P predicate register in streaming Scalable Vector Extension (SVE) mode.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func hv_vcpu_get_sme_p_reg(_ vcpu: hv_vcpu_t, _ reg: hv_sme_p_reg_t, _ value: UnsafeMutablePointer<UInt8>, _ length: Int) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_get_sme_p_reg(hv_vcpu_t vcpu, hv_sme_p_reg_t reg, uint8_t *value, size_t length);
```

#### Return Value

`HV_SUCCESS` on success; otherwise an error code.

## Parameters

- `vcpu`: The vCPU ID of the vCPU instance
- `reg`: ID of the P predicate register.
- `value`: The pointer to the retrieved register value.
- `length`: The length of the provided value storage, in bytes.

## See Also

### Functions
- [func hv_sme_config_get_max_svl_bytes(UnsafeMutablePointer<Int>) -> hv_return_t](./hv_sme_config_get_max_svl_bytes%28_%29.md)
- [func hv_vcpu_apic_ctrl(hv_vcpuid_t, hv_apic_ctrl_t) -> hv_return_t](./hv_vcpu_apic_ctrl%28_,_%29.md)
- [func hv_vcpu_apic_get_state(hv_vcpuid_t, UnsafeMutablePointer<hv_apic_state_ext_t>) -> hv_return_t](./hv_vcpu_apic_get_state%28_,_%29.md)
- [func hv_vcpu_apic_lsc_enter_imm32(hv_vcpuid_t, UInt64, UInt32, UInt16, UInt32, UnsafeMutablePointer<UInt64>?, UInt32) -> hv_return_t](./hv_vcpu_apic_lsc_enter_imm32%28_,_,_,_,_,_,_%29.md)
- [func hv_vcpu_apic_lsc_enter_r32(hv_vcpuid_t, Bool, UInt64, UInt32, UInt16, hv_x86_reg_t, UnsafeMutablePointer<UInt64>?, UInt32) -> hv_return_t](./hv_vcpu_apic_lsc_enter_r32%28_,_,_,_,_,_,_,_%29.md)
- [func hv_vcpu_apic_lsc_invalidate(hv_vcpuid_t) -> hv_return_t](./hv_vcpu_apic_lsc_invalidate%28_%29.md)
- [func hv_vcpu_apic_put_state(hv_vcpuid_t, UnsafePointer<hv_apic_state_ext_t>) -> hv_return_t](./hv_vcpu_apic_put_state%28_,_%29.md)
- [func hv_vcpu_apic_read(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt32>) -> hv_return_t](./hv_vcpu_apic_read%28_,_,_%29.md)
- [func hv_vcpu_apic_trigger_lvt(hv_vcpuid_t, hv_apic_lvt_flavor_t) -> hv_return_t](./hv_vcpu_apic_trigger_lvt%28_,_%29.md)
- [func hv_vcpu_apic_write(hv_vcpuid_t, UInt32, UInt32, UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vcpu_apic_write%28_,_,_,_%29.md)
- [func hv_vcpu_exit_apic_access_read(hv_vcpuid_t, UnsafeMutablePointer<UInt32>) -> hv_return_t](./hv_vcpu_exit_apic_access_read%28_,_%29.md)
- [func hv_vcpu_exit_info(hv_vcpuid_t, UnsafeMutablePointer<hv_vm_exitinfo_t>) -> hv_return_t](./hv_vcpu_exit_info%28_,_%29.md)
- [func hv_vcpu_exit_init_ap(hv_vcpuid_t, UnsafeMutablePointer<Bool>, UInt32) -> hv_return_t](./hv_vcpu_exit_init_ap%28_,_,_%29.md)
- [func hv_vcpu_exit_inject_excp(hv_vcpuid_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Bool>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vcpu_exit_inject_excp%28_,_,_,_,_%29.md)
- [func hv_vcpu_exit_ioapic_eoi(hv_vcpuid_t, UnsafeMutablePointer<UInt8>) -> hv_return_t](./hv_vcpu_exit_ioapic_eoi%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_sme_p_reg(_:_:_:_:))*