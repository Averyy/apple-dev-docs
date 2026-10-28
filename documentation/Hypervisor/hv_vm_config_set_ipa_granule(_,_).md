# hv_vm_config_set_ipa_granule(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 26.0+

## Declaration

```swift
func hv_vm_config_set_ipa_granule(_ config: hv_vm_config_t, _ granule: hv_ipa_granule_t) -> hv_return_t
```

```c
extern hv_return_t hv_vm_config_set_ipa_granule(hv_vm_config_t config, hv_ipa_granule_t granule);
```

## Return Value

HV_SUCCESS on success, an error code otherwise.

## Discussion

Set the intermediate physical address granule size in virtual machine configuration.

## Parameters

- `config`: Configuration.
- `granule`: Granule size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_config_set_ipa_granule(_:_:))*