# deviceCapture

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Type Property

The option to capture the device and terminate existing drivers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
static var deviceCapture: IOUSBHostObjectInitOptions { get }
```

```c
IOUSBHostObjectInitOptionsDeviceCapture
```

## Discussion

Callers must have either the com.apple.vm.device-access entitlement and the [`IOUSBHostDevice`](../iousbhostdevice.md) object from [`IOServiceAuthorize(_:_:)`](../../iokit/api-1514533-ioserviceauthorize.md) authorization, or have root privileges. Using this option terminates all clients and drivers of the [`IOUSBHostDevice`](../iousbhostdevice.md) and associated [`IOUSBHostInterface`](../../kernel/iousbhostinterface.md) clients, as well as the caller. Upon [`destroy()`](../iousbhostobject/destroy%28%29.md) of the [`IOUSBHostDevice`](../iousbhostdevice.md), the device resets and [`IOUSBHostInterface`](../../kernel/iousbhostinterface.md) reregisters for [IOKit](../../iokit/iokit.md) matching.

## See Also

### Options
- [IOUSBHostObjectInitOptionsNone](./iousbhostobjectinitoptionsnone.md)
  The default argument for initializing the host object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobjectinitoptions/devicecapture)*