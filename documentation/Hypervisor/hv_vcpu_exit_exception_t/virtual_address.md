# virtual_address

**Framework**: Hypervisor  
**Kind**: property  
**Role**: Instance Property

The vCPU virtual address of the exception.

**Availability**:
- macOS

## Declaration

```swift
var virtual_address: hv_exception_address_t
```

```c
hv_exception_address_t virtual_address;
```

## See Also

### Instance Properties
- [var physical_address: hv_ipa_t](./physical_address.md)
  The intermediate physical address of the exception in the client.
- [var syndrome: hv_exception_syndrome_t](./syndrome.md)
  The vCPU exception syndrome causing the exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_exception_t/virtual_address)*