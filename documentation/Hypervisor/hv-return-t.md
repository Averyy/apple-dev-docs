# hv_return_t

**Framework**: Hypervisor  
**Kind**: typealias

The return type of framework functions.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_return_t = mach_error_t
```

## Topics

### Return Values
- [var HV_SUCCESS: Int](hv_success.md)
  The operation completed successfully.
- [var HV_ERROR: Int](hv_error.md)
  The operation was unsuccessful.
- [var HV_BUSY: Int](hv_busy.md)
  The operation was unsuccessful because the owning resource was busy.
- [var HV_BAD_ARGUMENT: Int](hv_bad_argument.md)
  The operation was unsuccessful because the function call had an invalid argument.
- [var HV_NO_RESOURCES: Int](hv_no_resources.md)
  The operation was unsuccessful because the host had no resources available to complete the request.
- [var HV_NO_DEVICE: Int](hv_no_device.md)
  The operation was unsuccessful because no VM or vCPU was available.
- [var HV_UNSUPPORTED: Int](hv_unsupported.md)
  The operation requested isn’t supported by the hypervisor.

## See Also

- [Hypervisor Errors](hypervisor-errors.md)
  Return codes returned by framework functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_return_t)*