# hv_vcpu_exit_t

**Framework**: Hypervisor  
**Kind**: struct

Information about an exit from the vCPU to the host.

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_vcpu_exit_t
```

## Topics

### Instance Properties
- [var exception: hv_vcpu_exit_exception_t](hv_vcpu_exit_t/exception.md)
  Information about an exit exception from the vcpu to the host.
- [var reason: hv_exit_reason_t](hv_vcpu_exit_t/reason.md)
  Information about an exit from the vcpu to the host.
### Initializers
- [init()](hv_vcpu_exit_t/init.md)
  Creates a new exit reason structure.
- [init(reason: hv_exit_reason_t, exception: hv_vcpu_exit_exception_t)](hv_vcpu_exit_t/init(reason:exception:).md)
  Creates a new virtual cpu exit structure with a reason and exception that you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_t)*