# deviceCapture

**Framework**: IOUSBHost  
**Kind**: property

The option to capture the device and terminate existing drivers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
static var deviceCapture: IOUSBHostObjectInitOptions { get }
```

#### Discussion

Callers must have either the com.apple.vm.device-access entitlement and the [`IOUSBHostDevice`](iousbhostdevice.md) object from [`IOServiceAuthorize(_:_:)`](https://developer.apple.com/documentation/iokit/1514533-ioserviceauthorize) authorization, or have root privileges. Using this option terminates all clients and drivers of the [`IOUSBHostDevice`](iousbhostdevice.md) and associated [`IOUSBHostInterface`](https://developer.apple.com/documentation/kernel/iousbhostinterface) clients, as well as the caller. Upon [`destroy()`](iousbhostobject/destroy().md) of the [`IOUSBHostDevice`](iousbhostdevice.md), the device resets and [`IOUSBHostInterface`](https://developer.apple.com/documentation/kernel/iousbhostinterface) reregisters for [`IOKit`](https://developer.apple.com/documentation/iokit) matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobjectinitoptions/devicecapture)*