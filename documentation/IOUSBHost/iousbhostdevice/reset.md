# reset()

**Framework**: IOUSBHost  
**Kind**: method

Terminates the device and attempts to re-enumerate it.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func reset() throws
```

#### Discussion

This function resets and attempts to re-enumerate the USB device, and terminates the [`IOUSBHostDevice`](https://developer.apple.com/documentation/kernel/iousbhostdevice) and all of its child [`IOService`](https://developer.apple.com/documentation/kernel/ioservice) objects. If the reset is successful, it also creates and registers a new [`IOService`](https://developer.apple.com/documentation/kernel/ioservice) object after terminating the previous object. After the call returns successfully, the framework [`IOUSBHostDevice`](iousbhostdevice.md) no longer has a valid connection with the [`IOService`](https://developer.apple.com/documentation/kernel/ioservice) object.

> ❗ **Important**:  To use the re-enumerated device, you must create a new framework client using [`initWithIOService:options:queue:error:interestHandler:`](iousbhostobject/initwithioservice:options:queue:error:interesthandler:.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/reset())*