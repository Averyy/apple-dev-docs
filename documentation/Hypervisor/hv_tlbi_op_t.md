# hv_tlbi_op_t

**Framework**: Hypervisor  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct hv_tlbi_op_t
```

```c
typedef enum { ... } hv_tlbi_op_t;
```

#### Overview

TLB invalidation operations for hv_vcpu_invalidate_tlb().

## Topics

### Initializers
- [init(UInt16)](./hv_tlbi_op_t/init%28_%29.md)
- [init(rawValue: UInt16)](./hv_tlbi_op_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt16](./hv_tlbi_op_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_tlbi_op_t)*