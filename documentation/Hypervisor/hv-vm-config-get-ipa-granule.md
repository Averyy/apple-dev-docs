# hv_vm_config_get_ipa_granule(_:_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 26.0+

## Declaration

```swift
func hv_vm_config_get_ipa_granule(_ config: hv_vm_config_t, _ granule: UnsafeMutablePointer<hv_ipa_granule_t>) -> hv_return_t
```

#### Return Value

HV_SUCCESS on success, an error code otherwise.

#### Discussion

Return the intermediate physical address granule size in virtual machine configuration.

## Parameters

- `config`: Configuration.
- `granule`: Pointer to the currently configured granule size (written on success).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_config_get_ipa_granule(_:_:))*