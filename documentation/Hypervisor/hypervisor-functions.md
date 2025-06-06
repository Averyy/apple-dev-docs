# Hypervisor Functions

**Framework**: Hypervisor

## Topics

### Functions
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
- [func hv_vcpu_exit_startup_ap(hv_vcpuid_t, UnsafeMutablePointer<Bool>, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_exit_startup_ap(_:_:_:_:).md)
- [func hv_vcpu_get_idle_time(hv_vcpuid_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_idle_time(_:_:).md)
- [func hv_vcpu_get_sme_p_reg(hv_vcpu_t, hv_sme_p_reg_t, UnsafeMutablePointer<UInt8>, Int) -> hv_return_t](hv_vcpu_get_sme_p_reg(_:_:_:_:).md)
  Returns the value of a vCPU P predicate register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_get_sme_state(hv_vcpu_t, UnsafeMutablePointer<hv_vcpu_sme_state_t>) -> hv_return_t](hv_vcpu_get_sme_state(_:_:).md)
  Gets the current Scalable Matrix Extension (SME) state.
- [func hv_vcpu_get_sme_z_reg(hv_vcpu_t, hv_sme_z_reg_t, UnsafeMutablePointer<UInt8>, Int) -> hv_return_t](hv_vcpu_get_sme_z_reg(_:_:_:_:).md)
  Returns the value of a vCPU Z vector register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_get_sme_za_reg(hv_vcpu_t, UnsafeMutablePointer<UInt8>, Int) -> hv_return_t](hv_vcpu_get_sme_za_reg(_:_:_:).md)
  Returns the value of the vCPU ZA matrix register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_get_sme_zt0_reg(hv_vcpu_t, UnsafeMutablePointer<hv_sme_zt0_uchar64_t>) -> hv_return_t](hv_vcpu_get_sme_zt0_reg(_:_:).md)
  Returns the current value of the vCPU ZT0 register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_inject_extint(hv_vcpuid_t) -> hv_return_t](hv_vcpu_inject_extint(_:).md)
- [func hv_vcpu_set_sme_p_reg(hv_vcpu_t, hv_sme_p_reg_t, UnsafePointer<UInt8>, Int) -> hv_return_t](hv_vcpu_set_sme_p_reg(_:_:_:_:).md)
  Sets the value of a vCPU P predicate register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_set_sme_state(hv_vcpu_t, UnsafePointer<hv_vcpu_sme_state_t>) -> hv_return_t](hv_vcpu_set_sme_state(_:_:).md)
  Sets the SME state consisting of the streaming Scalable Vector Extension (SVE) mode and ZA storage enable.
- [func hv_vcpu_set_sme_z_reg(hv_vcpu_t, hv_sme_z_reg_t, UnsafePointer<UInt8>, Int) -> hv_return_t](hv_vcpu_set_sme_z_reg(_:_:_:_:).md)
  Sets the value of a vCPU Z vector register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_set_sme_za_reg(hv_vcpu_t, UnsafePointer<UInt8>, Int) -> hv_return_t](hv_vcpu_set_sme_za_reg(_:_:_:).md)
  Sets the value of the vCPU ZA matrix register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_set_sme_zt0_reg(hv_vcpu_t, UnsafePointer<hv_sme_zt0_uchar64_t>) -> hv_return_t](hv_vcpu_set_sme_zt0_reg(_:_:).md)
  Sets the value of the vCPU ZT0 register in streaming Scalable Vector Extension (SVE) mode.
- [func hv_vcpu_vmx_status(hv_vcpuid_t, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vcpu_vmx_status(_:_:).md)
- [func hv_vm_allocate(UnsafeMutablePointer<UnsafeMutableRawPointer?>, Int, hv_allocate_flags_t) -> hv_return_t](hv_vm_allocate(_:_:_:).md)
- [func hv_vm_atpic_assert_irq(Int32) -> hv_return_t](hv_vm_atpic_assert_irq(_:).md)
- [func hv_vm_atpic_deassert_irq(Int32) -> hv_return_t](hv_vm_atpic_deassert_irq(_:).md)
- [func hv_vm_atpic_get_state(UnsafeMutablePointer<hv_atpic_state_ext_t>, Bool) -> hv_return_t](hv_vm_atpic_get_state(_:_:).md)
- [func hv_vm_atpic_port_read(Int32, UnsafeMutablePointer<UInt8>) -> hv_return_t](hv_vm_atpic_port_read(_:_:).md)
- [func hv_vm_atpic_port_write(Int32, UInt8) -> hv_return_t](hv_vm_atpic_port_write(_:_:).md)
- [func hv_vm_atpic_put_state(UnsafePointer<hv_atpic_state_ext_t>, Bool) -> hv_return_t](hv_vm_atpic_put_state(_:_:).md)
- [func hv_vm_config_get_default_ipa_size(UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_config_get_default_ipa_size(_:).md)
- [func hv_vm_config_get_ipa_size(hv_vm_config_t, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_config_get_ipa_size(_:_:).md)
- [func hv_vm_config_get_max_ipa_size(UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_config_get_max_ipa_size(_:).md)
- [func hv_vm_config_set_ipa_size(hv_vm_config_t, UInt32) -> hv_return_t](hv_vm_config_set_ipa_size(_:_:).md)
- [func hv_vm_deallocate(UnsafeMutableRawPointer, Int) -> hv_return_t](hv_vm_deallocate(_:_:).md)
- [func hv_vm_ioapic_assert_irq(Int32) -> hv_return_t](hv_vm_ioapic_assert_irq(_:).md)
- [func hv_vm_ioapic_deassert_irq(Int32) -> hv_return_t](hv_vm_ioapic_deassert_irq(_:).md)
- [func hv_vm_ioapic_get_state(UnsafeMutablePointer<hv_ioapic_state_ext_t>) -> hv_return_t](hv_vm_ioapic_get_state(_:).md)
- [func hv_vm_ioapic_pulse_irq(Int32) -> hv_return_t](hv_vm_ioapic_pulse_irq(_:).md)
- [func hv_vm_ioapic_put_state(UnsafePointer<hv_ioapic_state_ext_t>) -> hv_return_t](hv_vm_ioapic_put_state(_:).md)
- [func hv_vm_ioapic_read(hv_gpaddr_t, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_ioapic_read(_:_:).md)
- [func hv_vm_ioapic_write(hv_gpaddr_t, UInt32) -> hv_return_t](hv_vm_ioapic_write(_:_:).md)
- [func hv_vm_lapic_msi(UInt64, UInt64) -> hv_return_t](hv_vm_lapic_msi(_:_:).md)
- [func hv_vm_lapic_set_intr(hv_vcpuid_t, UInt8, hv_apic_intr_trigger_t) -> hv_return_t](hv_vm_lapic_set_intr(_:_:_:).md)
- [func hv_vm_map_space(hv_vm_space_t, hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_map_space(_:_:_:_:_:).md)
  Maps a region in the virtual address space of the current task into a guest physical address space of the VM.
- [func hv_vm_protect_space(hv_vm_space_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect_space(_:_:_:_:).md)
  Modifies the permissions of a region in a guest physical address space of the VM.
- [func hv_vm_send_ioapic_intr(UInt64) -> hv_return_t](hv_vm_send_ioapic_intr(_:).md)
- [func hv_vm_set_apic_bus_freq(UInt64) -> hv_return_t](hv_vm_set_apic_bus_freq(_:).md)
- [func hv_vm_space_create(UnsafeMutablePointer<hv_vm_space_t>) -> hv_return_t](hv_vm_space_create(_:).md)
  Creates an additional guest address space for the current task.
- [func hv_vm_space_destroy(hv_vm_space_t) -> hv_return_t](hv_vm_space_destroy(_:).md)
  Destroys the address space instance associated with the current task.
- [func hv_vm_unmap_space(hv_vm_space_t, hv_gpaddr_t, Int) -> hv_return_t](hv_vm_unmap_space(_:_:_:).md)
  Umaps a region in a guest physical address space of the VM.
- [func hv_vmx_vcpu_set_apic_address_space(hv_vcpuid_t, hv_vm_space_t, hv_gpaddr_t) -> hv_return_t](hv_vmx_vcpu_set_apic_address_space(_:_:_:).md)

## See Also

- [Hypervisor Structures](hypervisor-structures.md)
- [Hypervisor Constants](hypervisor-constants.md)
- [Hypervisor Data Types](hypervisor-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hypervisor-functions)*