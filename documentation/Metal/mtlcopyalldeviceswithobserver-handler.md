# MTLCopyAllDevicesWithObserver(handler:)

**Framework**: Metal  
**Kind**: func

Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.

**Availability**:
- macOS 10.13+
- Swift 4.0+

## Declaration

```swift
func MTLCopyAllDevicesWithObserver(handler: @escaping MTLDeviceNotificationHandler) -> (devices: [any MTLDevice], observer: NSObject)
```

#### Return Value

#### Discussion

Keep a copy of `observer` in your app in case you want to stop receiving notifications. You can stop receiving notifications by passing `observer` to the [`MTLRemoveDeviceObserver(_:)`](mtlremovedeviceobserver(_:).md) function.

## Parameters

- `handler`: A notification handler you implement that Metal calls when the system adds or removes a GPU device from the system.

## See Also

- [Finding Multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)
  Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that Drives a View’s Display](getting-the-gpu-that-drives-a-views-display.md)
  Keep up to date with the optimal device for your display.
- [func MTLCopyAllDevices() -> [any MTLDevice]](mtlcopyalldevices().md)
  Returns an array of all the Metal device instances in the system.
- [func MTLRemoveDeviceObserver(any NSObjectProtocol)](mtlremovedeviceobserver(_:).md)
  Removes a registered observer of device notifications.
- [func CGDirectDisplayCopyCurrentMetalDevice(_ display: CGDirectDisplayID) -> (any MTLDevice)?](../CoreGraphics/CGDirectDisplayCopyCurrentMetalDevice(_:).md)
  Returns the GPU device instance that’s currently driving a display.
- [typealias MTLDeviceNotificationHandler](mtldevicenotificationhandler.md)
  A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.
- [struct MTLDeviceNotificationName](mtldevicenotificationname.md)
  A notification that represents a change to a GPU device in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcopyalldeviceswithobserver(handler:))*