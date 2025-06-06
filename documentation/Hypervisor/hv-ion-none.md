# HV_ION_NONE

**Framework**: Hypervisor  
**Kind**: var

The value that represents a request for no notifications.

**Availability**:
- macOS ?+

## Declaration

```swift
var HV_ION_NONE: Int { get }
```

#### Discussion

Use this value to clear the I/O notifier’s notification request mask when you no longer want to receive notifications for any notifier event type. This only stops the delivery of notifications, it doesn’t remove notifiers. To remove a specific notifier use [`hv_vm_remove_pio_notifier(_:_:_:_:_:)`](hv_vm_remove_pio_notifier(_:_:_:_:_:).md).

## See Also

- [var HV_ION_ANY_SIZE: Int](hv_ion_any_size.md)
  The value that represents a request for notifications of an I/O result of any size.
- [var HV_ION_ANY_VALUE: Int](hv_ion_any_value.md)
  The value that represents a request for notifications of an I/O result that contains any value.
- [var HV_ION_EXIT_FULL: Int](hv_ion_exit_full.md)
  The value that represents a request for notifications if the I/O queue is full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ion_none)*