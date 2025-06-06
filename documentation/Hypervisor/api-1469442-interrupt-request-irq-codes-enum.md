# Interrupt request (IRQ) codes

**Framework**: Hypervisor

An enumeration that describes available interrupt codes.

## Topics

### IRQ codes
- [var IRQ_INFO_EXT_IRQ: UInt32](irq_info_ext_irq.md)
  The value that represents an external interrupt.
- [var IRQ_INFO_NMI: UInt32](irq_info_nmi.md)
  The value that represents a non-maskable-interrupt.
- [var IRQ_INFO_HARD_EXC: UInt32](irq_info_hard_exc.md)
  The value that represents a hardware exception.
- [var IRQ_INFO_SOFT_IRQ: UInt32](irq_info_soft_irq.md)
  The value that represents a software interrupt.
- [var IRQ_INFO_PRIV_SOFT_EXC: UInt32](irq_info_priv_soft_exc.md)
  The value that represents a privileged software exception.
- [var IRQ_INFO_SOFT_EXC: UInt32](irq_info_soft_exc.md)
  The value that represents a software exception interrupt.
- [var IRQ_INFO_ERROR_VALID: UInt32](irq_info_error_valid.md)
  The value that indicates the error associated with the interrupt is valid and is readable from the VMCS.
- [var IRQ_INFO_VALID: UInt32](irq_info_valid.md)
  The value that represents the interrupt is valid.
- [var IRQ_INFO_TYPE_MASK: UInt32](irq_info_type_mask.md)
  The value that represents the interrupt mask.

## See Also

- [VMX Creation Behavior](1469509-vmx_creation_behavior-enum.md)
  An enumeration that describes VMX creation behavior options.
- [VMX Exit Reasons](1469470-vmx-exit-reasons.md)
  An enumertion that describes the VMX exit reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/1469442-interrupt_request_irq_codes-enum)*