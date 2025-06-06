# hv_vcpu_config_get_feature_reg(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Gets the value of a feature register.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_config_get_feature_reg(_ config: hv_vcpu_config_t, _ feature_reg: hv_feature_reg_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

## Parameters

- `config`: The vCPU configuration.
- `feature_reg`: The ID of the feature register.
- `value`: The value of   on output. Undefined if the call doesn’t succeed.

## See Also

- [func hv_vcpu_config_create() -> hv_vcpu_config_t](hv_vcpu_config_create().md)
  Creates a vCPU configuration object.
- [func hv_vcpu_config_get_ccsidr_el1_sys_reg_values(hv_vcpu_config_t, hv_cache_type_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_config_get_ccsidr_el1_sys_reg_values(_:_:_:).md)
  Returns the Cache Size ID Register (CCSIDR_EL1) values for the vCPU configuration and cache type you specify.
- [typealias hv_vcpu_config_t](hv_vcpu_config_t.md)
  The type that defines a vCPU configuration.
- [protocol OS_hv_vcpu_config](os_hv_vcpu_config.md)
  Configuration for a virtual CPU.
- [struct hv_feature_reg_t](hv_feature_reg_t.md)
  The type that defines feature registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_config_get_feature_reg(_:_:_:))*