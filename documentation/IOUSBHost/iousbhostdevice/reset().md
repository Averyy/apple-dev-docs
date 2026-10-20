# reset()

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Terminates the device and attempts to re-enumerate it.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func reset() throws
```

```objc
- (BOOL) resetWithError:(NSError **) error;
```

#### Discussion

This function resets and attempts to re-enumerate the USB device, and terminates the [`IOUSBHostDevice`](../../kernel/iousbhostdevice.md) and all of its child [`IOService`](../../kernel/ioservice.md) objects. If the reset is successful, it also creates and registers a new [`IOService`](../../kernel/ioservice.md) object after terminating the previous object. After the call returns successfully, the framework [`IOUSBHostDevice`](../iousbhostdevice.md) no longer has a valid connection with the [`IOService`](../../kernel/ioservice.md) object.

> ❗ **Important**:  To use the re-enumerated device, you must create a new framework client using [`initWithIOService:options:queue:error:interestHandler:`](../iousbhostobject/initwithioservice_options_queue_error_interesthandler_.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/reset())*