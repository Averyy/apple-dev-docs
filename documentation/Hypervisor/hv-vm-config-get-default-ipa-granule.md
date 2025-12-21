# hv_vm_config_get_default_ipa_granule(_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 26.0+

## Declaration

```swift
func hv_vm_config_get_default_ipa_granule(_ granule: UnsafeMutablePointer<hv_ipa_granule_t>) -> hv_return_t
```

#### Return Value

HV_SUCCESS on success, an error code otherwise.

#### Discussion

Return the default intermediate physical address granule.

## Parameters

- `granule`: Pointer to the default intermediate physical address granule size (written on success).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_config_get_default_ipa_granule(_:))*