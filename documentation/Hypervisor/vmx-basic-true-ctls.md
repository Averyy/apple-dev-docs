# VMX_BASIC_TRUE_CTLS

**Framework**: Hypervisor  
**Kind**: var

This bit field, in the value returned by the IA32_VMX_BASIC model specific register, determines if it’s possible to disable any VMX controls.

**Availability**:
- macOS ?+

## Declaration

```swift
var VMX_BASIC_TRUE_CTLS: UInt { get }
```

#### Discussion

The hardware must return this bit as a 1 in order to create any VM using the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/vmx_basic_true_ctls)*