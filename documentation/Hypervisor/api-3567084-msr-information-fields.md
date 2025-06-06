# MSR Information Fields

**Framework**: Hypervisor

The type that describes Machine Specific Register (MSR) fields.

## Topics

### Fields
- [var HV_VMX_INFO_MSR_IA32_ARCH_CAPABILITIES: Int](hv_vmx_info_msr_ia32_arch_capabilities.md)
  The value of the IA32 architecture capabilities model specific register.
- [var HV_VMX_INFO_MSR_IA32_PERF_CAPABILITIES: Int](hv_vmx_info_msr_ia32_perf_capabilities.md)
  The value of the IA32 performance capabilities model specific register.
- [var HV_VMX_VALID_MSR_IA32_PERFEVNTSEL: Int](hv_vmx_valid_msr_ia32_perfevntsel.md)
  The bitmask of the supported fields of the IA32 Performance-Event Selection Mode model specific register.
- [var HV_VMX_VALID_MSR_IA32_FIXED_CTR_CTRL: Int](hv_vmx_valid_msr_ia32_fixed_ctr_ctrl.md)
  The bitmask fo the supported fields of the Fixed-Function-Counter Control Register.
- [var HV_VMX_VALID_MSR_IA32_PERF_GLOBAL_CTRL: Int](hv_vmx_valid_msr_ia32_perf_global_ctrl.md)
  The bitmask of the supported fields of the IA32 Global-Counter Control Facility Register.
- [var HV_VMX_VALID_MSR_IA32_PERF_GLOBAL_STATUS: Int](hv_vmx_valid_msr_ia32_perf_global_status.md)
  The bitmast of the supported fields of the Global-Counter-Control Status model specific register.
- [var HV_VMX_VALID_MSR_IA32_DEBUGCTL: Int](hv_vmx_valid_msr_ia32_debugctl.md)
  The bitmask of the IA32 Debug-Control model specific register.
- [var HV_VMX_VALID_MSR_IA32_SPEC_CTRL: Int](hv_vmx_valid_msr_ia32_spec_ctrl.md)
  The bitmask of the suppported fields of the Speculation Control model specific register.
- [var HV_VMX_NEED_MSR_IA32_SPEC_CTRL: Int](hv_vmx_need_msr_ia32_spec_ctrl.md)
  The bitmask of the required fields of the IA32 Speculation Control model specific register.

## See Also

- [func hv_vmx_read_capability(hv_vmx_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_read_capability(_:_:).md)
  Returns, by reference, the VMX virtualization capabilities of the host processor.
- [func hv_vmx_get_msr_info(hv_vmx_msr_info_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_get_msr_info(_:_:).md)
  Returns information about guest MSR configuration.
- [struct hv_vmx_capability_t](hv_vmx_capability_t.md)
  The type that describes Virtual Machine Extensions (VMX) capability fields.
- [VMX Capabilities](1469645-vmx-capabilities.md)
  An enumeration that represents the available VMX capabilities.
- [typealias hv_vmx_msr_info_t](hv_vmx_msr_info_t.md)
  The type that describes Move to Status Register (MSR) information fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/3567084-msr-information-fields)*