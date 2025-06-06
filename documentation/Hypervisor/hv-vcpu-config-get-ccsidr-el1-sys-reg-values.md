# hv_vcpu_config_get_ccsidr_el1_sys_reg_values(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns the Cache Size ID Register (CCSIDR_EL1) values for the vCPU configuration and cache type you specify.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_config_get_ccsidr_el1_sys_reg_values(_ config: hv_vcpu_config_t, _ cache_type: hv_cache_type_t, _ values: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

A [`hv_return_t`](hv_return_t.md) value that indicates that result of the function.

## Parameters

- `config`: The vCPU configuration.
- `cache_type`: The cache type from the available   types.
- `values`: A pointer to the location for the return values.

## See Also

- [func hv_vcpu_config_create() -> hv_vcpu_config_t](hv_vcpu_config_create().md)
  Creates a vCPU configuration object.
- [func hv_vcpu_config_get_feature_reg(hv_vcpu_config_t, hv_feature_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_config_get_feature_reg(_:_:_:).md)
  Gets the value of a feature register.
- [typealias hv_vcpu_config_t](hv_vcpu_config_t.md)
  The type that defines a vCPU configuration.
- [protocol OS_hv_vcpu_config](os_hv_vcpu_config.md)
  Configuration for a virtual CPU.
- [struct hv_feature_reg_t](hv_feature_reg_t.md)
  The type that defines feature registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_config_get_ccsidr_el1_sys_reg_values(_:_:_:))*