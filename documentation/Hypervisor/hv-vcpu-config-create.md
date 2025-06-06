# hv_vcpu_config_create()

**Framework**: Hypervisor  
**Kind**: func

Creates a vCPU configuration object.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_config_create() -> hv_vcpu_config_t
```

#### Return Value

A new vCPU configuration object.

#### Discussion

If your app isn’t using ARC, call [`os_release`](https://developer.apple.com/documentation/os/1524245-os_release) on a vCPU configuration object when it’s no longer needed.

## See Also

- [func hv_vcpu_config_get_feature_reg(hv_vcpu_config_t, hv_feature_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_config_get_feature_reg(_:_:_:).md)
  Gets the value of a feature register.
- [func hv_vcpu_config_get_ccsidr_el1_sys_reg_values(hv_vcpu_config_t, hv_cache_type_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_config_get_ccsidr_el1_sys_reg_values(_:_:_:).md)
  Returns the Cache Size ID Register (CCSIDR_EL1) values for the vCPU configuration and cache type you specify.
- [typealias hv_vcpu_config_t](hv_vcpu_config_t.md)
  The type that defines a vCPU configuration.
- [protocol OS_hv_vcpu_config](os_hv_vcpu_config.md)
  Configuration for a virtual CPU.
- [struct hv_feature_reg_t](hv_feature_reg_t.md)
  The type that defines feature registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_config_create())*