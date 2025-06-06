# OS_hv_gic_config

**Framework**: Hypervisor  
**Kind**: protocol

Methods that provide information on the state of a generic interrupt controller.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol OS_hv_gic_config : NSObjectProtocol
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [typealias hv_gic_config_t](hv_gic_config_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) configuration’s reference type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/os_hv_gic_config)*