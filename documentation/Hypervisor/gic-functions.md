# GIC functions

**Framework**: Hypervisor

These functions and registers support the creation and operation of a generic interrupt controller.

#### Discussion

For more information on using GICs, see the [`ARM Generic Interrupt Controller (GIC) v3 architecture specification`](https://developer.apple.comhttps://developer.arm.com/documentation/ihi0069/latest/).

## Topics

### Creating a generic interrupt controller
- [func hv_gic_create(hv_gic_config_t) -> hv_return_t](hv_gic_create(_:).md)
  Creates a generic interrupt controller (GIC) v3 device for a VM configuration.
### Resetting the generic interrupt controller
- [func hv_gic_reset() -> hv_return_t](hv_gic_reset().md)
  Resets the generic interrupt controller (GIC) device.
### Setting the GIC device configuration
- [func hv_gic_config_create() -> hv_gic_config_t](hv_gic_config_create().md)
  Creates a generic interrupt controller (GIC) configuration object.
- [func hv_gic_config_set_distributor_base(hv_gic_config_t, hv_ipa_t) -> hv_return_t](hv_gic_config_set_distributor_base(_:_:).md)
  Sets the generic interrupt controller (GIC) distributor region’s base address.
- [func hv_gic_config_set_redistributor_base(hv_gic_config_t, hv_ipa_t) -> hv_return_t](hv_gic_config_set_redistributor_base(_:_:).md)
  Sets the generic interrupt controller (GIC) redistributor region base address.
- [func hv_gic_get_redistributor_base(hv_vcpu_t, UnsafeMutablePointer<hv_ipa_t>) -> hv_return_t](hv_gic_get_redistributor_base(_:_:).md)
  Gets the redistributor base guest physical address for the given vCPU.
- [func hv_gic_config_set_msi_region_base(hv_gic_config_t, hv_ipa_t) -> hv_return_t](hv_gic_config_set_msi_region_base(_:_:).md)
  Sets the generic interrupt controllers message signaled interrupts (MSIs) region base address.
- [func hv_gic_config_set_msi_interrupt_range(hv_gic_config_t, UInt32, UInt32) -> hv_return_t](hv_gic_config_set_msi_interrupt_range(_:_:_:).md)
  Sets the range of message signaled interrupts (MSIs) the generic interrupt controller supports.
- [protocol OS_hv_gic_config](os_hv_gic_config.md)
  Methods that provide information on the state of a generic interrupt controller.
- [typealias hv_gic_config_t](hv_gic_config_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) configuration’s reference type.
### Getting GIC device parameters
- [func hv_gic_get_redistributor_region_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_redistributor_region_size(_:).md)
  Gets the total size in bytes of the generic interrupt controller (GIC) redistributor region.
- [func hv_gic_get_redistributor_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_redistributor_size(_:).md)
  Gets the size in bytes of a single generic interrupt controller (GIC) redistributor.
- [func hv_gic_get_distributor_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_distributor_size(_:).md)
  Gets the size of the generic interrupt controller (GIC) distributor region, in bytes.
- [func hv_gic_get_distributor_base_alignment(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_distributor_base_alignment(_:).md)
  Gets the alignment for the base address of the generic interrupt controller (GIC) distributor region, in bytes.
- [func hv_gic_get_redistributor_base_alignment(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_redistributor_base_alignment(_:).md)
  Gets the alignment for the base address of the generic interrupt controller (GIC) redistributor region, in bytes.
- [func hv_gic_get_msi_region_base_alignment(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_msi_region_base_alignment(_:).md)
  Gets the alignment, in bytes, for the base address of the generic interrupt controller’s message signaled interrupts (MSI) region.
- [func hv_gic_get_msi_region_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_msi_region_size(_:).md)
  Gets the size in bytes of the generic interrupt controller’s (GIC) message signaled interrupts (MSI) region.
- [func hv_gic_get_spi_interrupt_range(UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_gic_get_spi_interrupt_range(_:_:).md)
  Gets the range of shared peripheral interrupts (SPIs) the generic interrupt controller supports.
### Getting and setting the GIC’s state
- [func hv_gic_state_create() -> hv_gic_state_t](hv_gic_state_create().md)
  Create a generic interrupt controller (GIC) state object.
- [func hv_gic_set_state(UnsafeRawPointer, Int) -> hv_return_t](hv_gic_set_state(_:_:).md)
  Sets the state of a generic interrupt controller (GIC) device.
- [func hv_gic_state_get_size(hv_gic_state_t, UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_state_get_size(_:_:).md)
  Gets the size of the buffer required for generic interrupt controller (GIC) state.
- [func hv_gic_state_get_data(hv_gic_state_t, UnsafeMutableRawPointer) -> hv_return_t](hv_gic_state_get_data(_:_:).md)
  Gets the state data for generic interrupt controller (GIC).
- [typealias hv_gic_state_t](hv_gic_state_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.
- [protocol OS_hv_gic_state](os_hv_gic_state.md)
  Methods that provide information on the hypervisor state.
### Sending interrupts
- [func hv_gic_send_msi(hv_ipa_t, UInt32) -> hv_return_t](hv_gic_send_msi(_:_:).md)
  Sends a message signaled interrupt (MSI).
- [func hv_gic_set_spi(UInt32, Bool) -> hv_return_t](hv_gic_set_spi(_:_:).md)
  Triggers a shared peripheral interrupt (SPI).
### Getting and setting registers
- [func hv_gic_get_distributor_reg(hv_gic_distributor_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_gic_get_distributor_reg(_:_:).md)
  Reads a generic interrupt controller (GIC) distributor register.
- [func hv_gic_get_msi_reg(hv_gic_msi_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_gic_get_msi_reg(_:_:).md)
  Reads a generic interrupt controller (GIC) distributor message signaled interrupt (MSI) register.
- [func hv_gic_get_icc_reg(hv_vcpu_t, hv_gic_icc_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_gic_get_icc_reg(_:_:_:).md)
  Reads a generic interrupt controller’s ICC CPU system register.
- [func hv_gic_get_ich_reg(hv_vcpu_t, hv_gic_ich_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_gic_get_ich_reg(_:_:_:).md)
  Reads a generic interrupt controller’s (GIC) ICH virtualization control system register.
- [func hv_gic_get_icv_reg(hv_vcpu_t, hv_gic_icv_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_gic_get_icv_reg(_:_:_:).md)
  Writes a generic interrupt controller’s (GIC) ICV system register.
- [func hv_gic_get_redistributor_reg(hv_vcpu_t, hv_gic_redistributor_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_gic_get_redistributor_reg(_:_:_:).md)
  Read a generic interrupt controller (GIC) redistributor register.
- [func hv_gic_set_distributor_reg(hv_gic_distributor_reg_t, UInt64) -> hv_return_t](hv_gic_set_distributor_reg(_:_:).md)
  Writes the provided value to a generic interrupt controller (GIC) distributor register you specify.
- [func hv_gic_set_icc_reg(hv_vcpu_t, hv_gic_icc_reg_t, UInt64) -> hv_return_t](hv_gic_set_icc_reg(_:_:_:).md)
  Writes to a generic interrupt controller (GIC) ICC cpu system register.
- [func hv_gic_set_ich_reg(hv_vcpu_t, hv_gic_ich_reg_t, UInt64) -> hv_return_t](hv_gic_set_ich_reg(_:_:_:).md)
  Writes to a generic interrupt controller (GIC) ICH virtualization control system register.
- [func hv_gic_set_icv_reg(hv_vcpu_t, hv_gic_icv_reg_t, UInt64) -> hv_return_t](hv_gic_set_icv_reg(_:_:_:).md)
  Writes to a generic interrupt controller (GIC) ICV system register.
- [func hv_gic_set_msi_reg(hv_gic_msi_reg_t, UInt64) -> hv_return_t](hv_gic_set_msi_reg(_:_:).md)
  Writes to a generic interrupt controller distributor message signaled interrupt (MSI) register.
- [func hv_gic_set_redistributor_reg(hv_vcpu_t, hv_gic_redistributor_reg_t, UInt64) -> hv_return_t](hv_gic_set_redistributor_reg(_:_:_:).md)
  Writes to a GIC redistributor register.

## See Also

- [GIC registers](gic-registers.md)
  These registers support the operation of a generic interrupt controller and its interface with the Hypervisor and virtual CPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/gic-functions)*