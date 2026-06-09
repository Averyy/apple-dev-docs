# hv_vcpu_set_serror(_:_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func hv_vcpu_set_serror(_ vcpu: hv_vcpu_t, _ pending: Bool) -> hv_return_t
```

#### Discussion

Sets pending SError for a vcpu.

Must be called by the owning thread.

## Parameters

- `vcpu`: ID of the vcpu instance.
- `pending`: Whether the SError is pending or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_set_serror(_:_:))*