# MTLCopyAllDevicesWithObserver

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.

**Availability**:
- macOS 10.13+ - Deprecated in 27.0

## Declaration

```c
extern NSArray<id<MTLDevice>> *MTLCopyAllDevicesWithObserver(id<NSObject>*observer, MTLDeviceNotificationHandler handler);
```

## Mentions

- [Handling external GPU additions and removals](./handling-external-gpu-additions-and-removals.md)
- [Finding multiple GPUs on an Intel-based Mac](./finding-multiple-gpus-on-an-intel-based-mac.md)

#### Discussion

Keep a copy of `observer` in your app after this function returns in case you want to stop receiving notifications. You can stop receiving notifications by passing `observer` to the [`MTLRemoveDeviceObserver(_:)`](./mtlremovedeviceobserver%28_%29.md) function.

## Parameters

- `observer`: A pointer to an object instance the method sets to a new observer — which Metal retains — before returning.
- `handler`: A notification handler you implement that Metal calls when the system adds or removes a GPU device from the system.

## See Also

### Locating GPUs
- [Finding multiple GPUs on an Intel-based Mac](./finding-multiple-gpus-on-an-intel-based-mac.md)
  Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](./getting-the-gpu-that-drives-a-views-display.md)
  Keep up to date with the optimal device for your display.
- [func MTLCopyAllDevices() -> [any MTLDevice]](./mtlcopyalldevices%28%29.md)
  Returns an array of all the Metal device instances in the system.
- [func MTLRemoveDeviceObserver(any NSObjectProtocol)](./mtlremovedeviceobserver%28_%29.md)
  Removes a registered observer of device notifications.
- [func CGDirectDisplayCopyCurrentMetalDevice(CGDirectDisplayID) -> (any MTLDevice)?](../CoreGraphics/cgdirectdisplaycopycurrentmetaldevice%28_%29.md)
  Returns the GPU device instance that’s currently driving a display.
- [typealias MTLDeviceNotificationHandler](./mtldevicenotificationhandler.md)
  A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.
- [struct MTLDeviceNotificationName](./mtldevicenotificationname.md)
  A notification that represents a change to a GPU device in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcopyalldeviceswithobserver)*