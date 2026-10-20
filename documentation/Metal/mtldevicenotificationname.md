# MTLDeviceNotificationName

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

A notification that represents a change to a GPU device in the system.

**Availability**:
- macOS 10.13+ - Deprecated in 27.0

> **Deprecated**: Device notifications are not applicable on Apple Silicon

## Declaration

```swift
struct MTLDeviceNotificationName
```

```c
typedef NSString * MTLDeviceNotificationName;
```

## Topics

### Creating a notification name
- [static let wasAdded: MTLDeviceNotificationName](./mtldevicenotificationname/wasadded.md)
  A notification that Metal sends to observers when the system adds a GPU device.
- [static let removalRequested: MTLDeviceNotificationName](./mtldevicenotificationname/removalrequested.md)
  A notification that Metal sends to observers when a person requests to remove a GPU device from the system.
- [static let wasRemoved: MTLDeviceNotificationName](./mtldevicenotificationname/wasremoved.md)
  A notification that Metal sends to observers when the system removes a GPU device.
- [init(rawValue: String)](./mtldevicenotificationname/init%28rawvalue%29.md)
  Creates a Metal device notification name from a string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [typealias MTLDeviceNotificationHandler](./mtldevicenotificationhandler.md)
  A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname)*