# physical_address

**Framework**: Hypervisor  
**Kind**: property  
**Role**: Instance Property

The intermediate physical address of the exception in the client.

**Availability**:
- macOS

## Declaration

```swift
var physical_address: hv_ipa_t
```

```c
hv_ipa_t physical_address;
```

## See Also

### Instance Properties
- [var syndrome: hv_exception_syndrome_t](./syndrome.md)
  The vCPU exception syndrome causing the exception.
- [var virtual_address: hv_exception_address_t](./virtual_address.md)
  The vCPU virtual address of the exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_exception_t/physical_address)*