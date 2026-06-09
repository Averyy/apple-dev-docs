# hv_vcpu_get_serror(_:_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func hv_vcpu_get_serror(_ vcpu: hv_vcpu_t, _ pending: UnsafeMutablePointer<Bool>) -> hv_return_t
```

#### Discussion

Gets pending SError for a vcpu.

Must be called by the owning thread.

## Parameters

- `vcpu`: ID of the vcpu instance.
- `pending`: Returns whether the SError is pending or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_serror(_:_:))*