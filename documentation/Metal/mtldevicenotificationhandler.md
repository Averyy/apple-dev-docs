# MTLDeviceNotificationHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.

**Availability**:
- macOS 10.13+ - Deprecated in 27.0

> **Deprecated**: Device notifications are not applicable on Apple Silicon

## Declaration

```swift
typealias MTLDeviceNotificationHandler = @Sendable (any MTLDevice, MTLDeviceNotificationName) -> Void
```

```c
typedef void (^)(id<MTLDevice>, NSString *) MTLDeviceNotificationHandler;
```

## Parameters

- `device`: An [`MTLDevice`](./mtldevice.md) that represents the GPU that’s sending the notification.
- `notifyName`: A notification that represents a change to a GPU device in the system.

## See Also

### Locating GPUs
- [Finding multiple GPUs on an Intel-based Mac](./finding-multiple-gpus-on-an-intel-based-mac.md)
  Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](./getting-the-gpu-that-drives-a-views-display.md)
  Keep up to date with the optimal device for your display.
- [func MTLCopyAllDevices() -> [any MTLDevice]](./mtlcopyalldevices%28%29.md)
  Returns an array of all the Metal device instances in the system.
- [func MTLCopyAllDevicesWithObserver(handler: (any MTLDevice, MTLDeviceNotificationName) -> Void) -> (devices: [any MTLDevice], observer: NSObject)](./mtlcopyalldeviceswithobserver%28handler%29.md)
  Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [func MTLRemoveDeviceObserver(any NSObjectProtocol)](./mtlremovedeviceobserver%28_%29.md)
  Removes a registered observer of device notifications.
- [func CGDirectDisplayCopyCurrentMetalDevice(CGDirectDisplayID) -> (any MTLDevice)?](../CoreGraphics/cgdirectdisplaycopycurrentmetaldevice%28_%29.md)
  Returns the GPU device instance that’s currently driving a display.
- [struct MTLDeviceNotificationName](./mtldevicenotificationname.md)
  A notification that represents a change to a GPU device in the system.
- [MTLCopyAllDevicesWithObserver](./mtlcopyalldeviceswithobserver.md)
  Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationhandler)*