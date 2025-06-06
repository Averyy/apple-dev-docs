# HV_GIC_INT_EL1_VIRTUAL_TIMER

**Framework**: Hypervisor  
**Kind**: var

**Availability**:
- macOS ?+

## Declaration

```swift
var HV_GIC_INT_EL1_VIRTUAL_TIMER: hv_gic_intid_t { get }
```

## See Also

- [func hv_gic_get_intid(hv_gic_intid_t, UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_gic_get_intid(_:_:).md)
  Gets the interrupt ID for reserved interrupts.
- [var HV_GIC_INT_MAINTENANCE: hv_gic_intid_t](hv_gic_int_maintenance.md)
  A register Hypervisor uses to signal virtual Interrupts (vIRQs) that the framework sends to guests running at exception level 2 (EL2).
- [var HV_GIC_INT_PERFORMANCE_MONITOR: hv_gic_intid_t](hv_gic_int_performance_monitor.md)
  A register the framework uses to count GIC related events.
- [var HV_GIC_INT_EL1_PHYSICAL_TIMER: hv_gic_intid_t](hv_gic_int_el1_physical_timer.md)
- [var HV_GIC_INT_EL2_PHYSICAL_TIMER: hv_gic_intid_t](hv_gic_int_el2_physical_timer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_int_el1_virtual_timer)*