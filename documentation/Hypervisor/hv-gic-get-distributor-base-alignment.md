# hv_gic_get_distributor_base_alignment(_:)

**Framework**: Hypervisor  
**Kind**: func

Gets the alignment for the base address of the generic interrupt controller (GIC) distributor region, in bytes.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_get_distributor_base_alignment(_ distributor_base_alignment: UnsafeMutablePointer<Int>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) on success; otherwise, an error code.

## Parameters

- `distributor_base_alignment`: A pointer to GIC distributor base address alignment value that the framework writes to upon success.

## See Also

- [func hv_gic_get_redistributor_region_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_redistributor_region_size(_:).md)
  Gets the total size in bytes of the generic interrupt controller (GIC) redistributor region.
- [func hv_gic_get_redistributor_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_redistributor_size(_:).md)
  Gets the size in bytes of a single generic interrupt controller (GIC) redistributor.
- [func hv_gic_get_distributor_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_distributor_size(_:).md)
  Gets the size of the generic interrupt controller (GIC) distributor region, in bytes.
- [func hv_gic_get_redistributor_base_alignment(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_redistributor_base_alignment(_:).md)
  Gets the alignment for the base address of the generic interrupt controller (GIC) redistributor region, in bytes.
- [func hv_gic_get_msi_region_base_alignment(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_msi_region_base_alignment(_:).md)
  Gets the alignment, in bytes, for the base address of the generic interrupt controller’s message signaled interrupts (MSI) region.
- [func hv_gic_get_msi_region_size(UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_get_msi_region_size(_:).md)
  Gets the size in bytes of the generic interrupt controller’s (GIC) message signaled interrupts (MSI) region.
- [func hv_gic_get_spi_interrupt_range(UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_gic_get_spi_interrupt_range(_:_:).md)
  Gets the range of shared peripheral interrupts (SPIs) the generic interrupt controller supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_get_distributor_base_alignment(_:))*