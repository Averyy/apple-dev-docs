# hv_gic_set_spi(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Triggers a shared peripheral interrupt (SPI).

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_set_spi(_ intid: UInt32, _ level: Bool) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) on success; otherwise, an error code.

#### Discussion

Setting a level value causes level interrupts. To cause an edge interrupt, call this method with a level of [`true`](https://developer.apple.com/documentation/Swift/true). The framework ignores a level of [`false`](https://developer.apple.com/documentation/Swift/false) for an edge interrupt.

An interrupt identifier outside of [`hv_gic_get_spi_interrupt_range(_:_:)`](hv_gic_get_spi_interrupt_range(_:_:).md) or in the message signaled interrupt (MSI) range returns a [`HV_BAD_ARGUMENT`](hv_bad_argument.md) error code.

## Parameters

- `intid`: The interrupt number of the SPI.
- `level`: The high- or low-level state for the interrupt. Setting the level also causes an edge on the line for an edge triggered interrupt.

## See Also

- [func hv_gic_send_msi(hv_ipa_t, UInt32) -> hv_return_t](hv_gic_send_msi(_:_:).md)
  Sends a message signaled interrupt (MSI).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_set_spi(_:_:))*