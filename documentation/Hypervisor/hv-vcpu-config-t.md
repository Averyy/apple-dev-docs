# hv_vcpu_config_t

**Framework**: Hypervisor  
**Kind**: typealias

The type that defines a vCPU configuration.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vcpu_config_t = any OS_hv_vcpu_config
```

## See Also

- [func hv_vcpu_config_create() -> hv_vcpu_config_t](hv_vcpu_config_create().md)
  Creates a vCPU configuration object.
- [func hv_vcpu_config_get_feature_reg(hv_vcpu_config_t, hv_feature_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_config_get_feature_reg(_:_:_:).md)
  Gets the value of a feature register.
- [func hv_vcpu_config_get_ccsidr_el1_sys_reg_values(hv_vcpu_config_t, hv_cache_type_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_config_get_ccsidr_el1_sys_reg_values(_:_:_:).md)
  Returns the Cache Size ID Register (CCSIDR_EL1) values for the vCPU configuration and cache type you specify.
- [protocol OS_hv_vcpu_config](os_hv_vcpu_config.md)
  Configuration for a virtual CPU.
- [struct hv_feature_reg_t](hv_feature_reg_t.md)
  The type that defines feature registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_config_t)*