# hv_vcpu_exit_t

**Framework**: Hypervisor  
**Kind**: struct  
**Role**: Structure

Information about an exit from the vCPU to the host.

**Availability**:
- macOS

## Declaration

```swift
struct hv_vcpu_exit_t
```

```c
typedef struct { ... } hv_vcpu_exit_t;
```

## Topics

### Instance Properties
- [var exception: hv_vcpu_exit_exception_t](./hv_vcpu_exit_t/exception.md)
  Information about an exit exception from the vcpu to the host.
- [var reason: hv_exit_reason_t](./hv_vcpu_exit_t/reason.md)
  Information about an exit from the vcpu to the host.
### Initializers
- [init()](./hv_vcpu_exit_t/init%28%29.md)
  Creates a new exit reason structure.
- [init(reason: hv_exit_reason_t, exception: hv_vcpu_exit_exception_t)](./hv_vcpu_exit_t/init%28reason,exception%29.md)
  Creates a new virtual cpu exit structure with a reason and exception that you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_t)*