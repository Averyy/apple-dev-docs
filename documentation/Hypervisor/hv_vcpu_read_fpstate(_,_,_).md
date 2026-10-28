# hv_vcpu_read_fpstate(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Returns, by reference, the current architectural x86 floating point and SIMD state of a vCPU.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vcpu_read_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutableRawPointer, _ size: Int) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_read_fpstate(hv_vcpuid_t vcpu, void *buffer, size_t size);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Discussion

The XSAVE feature set of the host processor defines the structure and size of the returned buffer.

> ❗ **Important**:  This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `buffer`: The floating point and SIMD state, on output.
- `size`: The size of `buffer`, in bytes.

## See Also

### Floating Point (FP) State
- [func hv_vcpu_write_fpstate(hv_vcpuid_t, UnsafeMutableRawPointer, Int) -> hv_return_t](./hv_vcpu_write_fpstate%28_,_,_%29.md)
  Sets the architectural x86 floating point and SIMD state of a vCPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_read_fpstate(_:_:_:))*