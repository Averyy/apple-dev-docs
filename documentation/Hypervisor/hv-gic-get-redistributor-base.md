# hv_gic_get_redistributor_base(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Gets the redistributor base guest physical address for the given vCPU.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_get_redistributor_base(_ vcpu: hv_vcpu_t, _ redistributor_base_address: UnsafeMutablePointer<hv_ipa_t>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) on success; otherwise, an error code.

#### Discussion

> ❗ **Important**:  Call this method after you set the affinity of the given vCPU in its `MPIDR_EL1` register.

## Parameters

- `vcpu`: Handle for the vCPU.
- `redistributor_base_address`: A pointer to the redistributor base guest physical address that the framework writes to upon success.

## See Also

- [func hv_gic_config_create() -> hv_gic_config_t](hv_gic_config_create().md)
  Creates a generic interrupt controller (GIC) configuration object.
- [func hv_gic_config_set_distributor_base(hv_gic_config_t, hv_ipa_t) -> hv_return_t](hv_gic_config_set_distributor_base(_:_:).md)
  Sets the generic interrupt controller (GIC) distributor region’s base address.
- [func hv_gic_config_set_redistributor_base(hv_gic_config_t, hv_ipa_t) -> hv_return_t](hv_gic_config_set_redistributor_base(_:_:).md)
  Sets the generic interrupt controller (GIC) redistributor region base address.
- [func hv_gic_config_set_msi_region_base(hv_gic_config_t, hv_ipa_t) -> hv_return_t](hv_gic_config_set_msi_region_base(_:_:).md)
  Sets the generic interrupt controllers message signaled interrupts (MSIs) region base address.
- [func hv_gic_config_set_msi_interrupt_range(hv_gic_config_t, UInt32, UInt32) -> hv_return_t](hv_gic_config_set_msi_interrupt_range(_:_:_:).md)
  Sets the range of message signaled interrupts (MSIs) the generic interrupt controller supports.
- [protocol OS_hv_gic_config](os_hv_gic_config.md)
  Methods that provide information on the state of a generic interrupt controller.
- [typealias hv_gic_config_t](hv_gic_config_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) configuration’s reference type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_get_redistributor_base(_:_:))*