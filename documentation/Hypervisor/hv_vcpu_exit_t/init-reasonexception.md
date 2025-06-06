# init(reason:exception:)

**Framework**: Hypervisor  
**Kind**: init

Creates a new virtual cpu exit structure with a reason and exception that you provide.

**Availability**:
- macOS ?+

## Declaration

```swift
init(reason: hv_exit_reason_t, exception: hv_vcpu_exit_exception_t)
```

## Parameters

- `reason`: The   result code that describes the reason for the exception.
- `exception`: The exception struture.

## See Also

- [init()](hv_vcpu_exit_t/init.md)
  Creates a new exit reason structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_t/init(reason:exception:))*