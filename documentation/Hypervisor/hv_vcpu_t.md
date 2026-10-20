# hv_vcpu_t

**Framework**: Hypervisor  
**Kind**: typealias  
**Role**: Type Alias

An opaque value that represents a vCPU instance.

**Availability**:
- macOS

## Declaration

```swift
typealias hv_vcpu_t = UInt64
```

```c
typedef uint64_t hv_vcpu_t;
```

## See Also

### Creation and destruction
- [func hv_vm_get_max_vcpu_count(UnsafeMutablePointer<UInt32>) -> hv_return_t](./hv_vm_get_max_vcpu_count%28_%29.md)
  Returns the maximum number of vCPUs that the hypervisor supports.
- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](./hv_vcpu_create%28_,_,_%29.md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](./hv_vcpu_destroy%28_%29.md)
  Destroys the vCPU instance associated with the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_t)*