# hv_vcpu_invalidate_tlb(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func hv_vcpu_invalidate_tlb(_ vcpu: hv_vcpu_t, _ op: hv_tlbi_op_t, _ param: UInt64) -> hv_return_t
```

#### Return Value

HV_SUCCESS on success, an error code otherwise.

#### Discussion

Invalidates TLB entries for the specified vCPU.

Must be called by the owning thread. When EL2 is enabled for this VM, this function invalidates TLB entries for the guest hypervisor, not the nested guests.

## Parameters

- `vcpu`: ID of the vCPU instance.
- `op`: TLB invalidation operation to perform.
- `param`: Parameter for the TLB operation (e.g., virtual address for VAAE1IS).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_invalidate_tlb(_:_:_:))*