# hv_vcpu_set_serror(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 27.0+

## Declaration

```swift
func hv_vcpu_set_serror(_ vcpu: hv_vcpu_t, _ pending: Bool) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_set_serror(hv_vcpu_t vcpu, bool pending);
```

#### Discussion

Sets pending SError for a vcpu.

Must be called by the owning thread.

## Parameters

- `vcpu`: ID of the vcpu instance.
- `pending`: Whether the SError is pending or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_set_serror(_:_:))*