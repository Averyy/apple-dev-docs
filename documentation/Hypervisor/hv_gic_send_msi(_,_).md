# hv_gic_send_msi(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Sends a message signaled interrupt (MSI).

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_send_msi(_ address: hv_ipa_t, _ intid: UInt32) -> hv_return_t
```

```c
extern hv_return_t hv_gic_send_msi(hv_ipa_t address, uint32_t intid);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) on success; otherwise, an error code.

## Discussion

Use the address of the [`HV_GIC_REG_GICM_SET_SPI_NSR`](./hv_gic_reg_gicm_set_spi_nsr.md) register in the MSI frame.

## Parameters

- `address`: The guest physical address for message-based shared peripheral interrupts (SPI).
- `intid`: The Interrupt identifier for the message based SPI.

## See Also

### Sending interrupts
- [func hv_gic_set_spi(UInt32, Bool) -> hv_return_t](./hv_gic_set_spi%28_,_%29.md)
  Triggers a shared peripheral interrupt (SPI).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_send_msi(_:_:))*