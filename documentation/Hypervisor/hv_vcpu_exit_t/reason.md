# reason

**Framework**: Hypervisor  
**Kind**: property  
**Role**: Instance Property

Information about an exit from the vcpu to the host.

**Availability**:
- macOS

## Declaration

```swift
var reason: hv_exit_reason_t
```

```c
hv_exit_reason_t reason;
```

## See Also

### Instance Properties
- [var exception: hv_vcpu_exit_exception_t](./exception.md)
  Information about an exit exception from the vcpu to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_t/reason)*