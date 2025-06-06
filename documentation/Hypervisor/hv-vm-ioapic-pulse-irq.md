# hv_vm_ioapic_pulse_irq(_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
func hv_vm_ioapic_pulse_irq(_ intin: Int32) -> hv_return_t
```

## See Also

- [func hv_sme_config_get_max_svl_bytes(UnsafeMutablePointer<Int>) -> hv_return_t](hv_sme_config_get_max_svl_bytes(_:).md)
- [func hv_vcpu_apic_ctrl(hv_vcpuid_t, hv_apic_ctrl_t) -> hv_return_t](hv_vcpu_apic_ctrl(_:_:).md)
- [func hv_vcpu_apic_get_state(hv_vcpuid_t, UnsafeMutablePointer<hv_apic_state_ext_t>) -> hv_return_t](hv_vcpu_apic_get_state(_:_:).md)
- [func hv_vcpu_apic_lsc_enter_imm32(hv_vcpuid_t, UInt64, UInt32, UInt16, UInt32, UnsafeMutablePointer<UInt64>?, UInt32) -> hv_return_t](hv_vcpu_apic_lsc_enter_imm32(_:_:_:_:_:_:_:).md)
- [func hv_vcpu_apic_lsc_enter_r32(hv_vcpuid_t, Bool, UInt64, UInt32, UInt16, hv_x86_reg_t, UnsafeMutablePointer<UInt64>?, UInt32) -> hv_return_t](hv_vcpu_apic_lsc_enter_r32(_:_:_:_:_:_:_:_:).md)
- [func hv_vcpu_apic_lsc_invalidate(hv_vcpuid_t) -> hv_return_t](hv_vcpu_apic_lsc_invalidate(_:).md)
- [func hv_vcpu_apic_put_state(hv_vcpuid_t, UnsafePointer<hv_apic_state_ext_t>) -> hv_return_t](hv_vcpu_apic_put_state(_:_:).md)
- [func hv_vcpu_apic_read(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vcpu_apic_read(_:_:_:).md)
- [func hv_vcpu_apic_trigger_lvt(hv_vcpuid_t, hv_apic_lvt_flavor_t) -> hv_return_t](hv_vcpu_apic_trigger_lvt(_:_:).md)
- [func hv_vcpu_apic_write(hv_vcpuid_t, UInt32, UInt32, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_apic_write(_:_:_:_:).md)
- [func hv_vcpu_exit_apic_access_read(hv_vcpuid_t, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vcpu_exit_apic_access_read(_:_:).md)
- [func hv_vcpu_exit_info(hv_vcpuid_t, UnsafeMutablePointer<hv_vm_exitinfo_t>) -> hv_return_t](hv_vcpu_exit_info(_:_:).md)
- [func hv_vcpu_exit_init_ap(hv_vcpuid_t, UnsafeMutablePointer<Bool>, UInt32) -> hv_return_t](hv_vcpu_exit_init_ap(_:_:_:).md)
- [func hv_vcpu_exit_inject_excp(hv_vcpuid_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Bool>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_exit_inject_excp(_:_:_:_:_:).md)
- [func hv_vcpu_exit_ioapic_eoi(hv_vcpuid_t, UnsafeMutablePointer<UInt8>) -> hv_return_t](hv_vcpu_exit_ioapic_eoi(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_ioapic_pulse_irq(_:))*