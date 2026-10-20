# init(syndrome:virtual_address:physical_address:)

**Framework**: Hypervisor  
**Kind**: init  
**Role**: Initializer

Creates a new VCPU exit exception instance.with the parameters you provide.

**Availability**:
- macOS

## Declaration

```swift
init(syndrome: hv_exception_syndrome_t, virtual_address: hv_exception_address_t, physical_address: hv_ipa_t)
```

## Parameters

- `syndrome`: The vCPU exception syndrome causing the exception.
- `virtual_address`: The vCPU virtual address of the exception.
- `physical_address`: The intermediate physical address of the exception in the client.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Creates a new VCPU exit exception instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_exception_t/init(syndrome:virtual_address:physical_address:))*