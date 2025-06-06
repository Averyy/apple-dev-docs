# Getting the GPU that Drives a View’s Display

**Framework**: Metal

Keep up to date with the optimal device for your display.

#### Overview

A user can have multiple external displays connected directly to a Mac or to an external GPU. Each view in your app shows on a single display, and a single GPU drives each display. The display in which your view appears and the GPU that drives the display can change dynamically; therefore, you need to prepare your app to handle these changes. Register for display change notifications, get the device that drives your view’s display, and decide if your app should use that device to present rendered graphics.

##### Handle Display Change Notifications

Register for the following notifications so the system can notify your app about specific display changes:

When the system posts a display change notification, you can decide if you should get and use a new device.

To deregister from the previous notifications, call the [`removeObserver(_:name:object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1407263-removeobserver) method.

##### Identify the Device That Drives Your Views Display

Get the [`CGDirectDisplayID`](https://developer.apple.com/documentation/CoreGraphics/CGDirectDisplayID) value for the display in which your view currently appears. Then call the [`CGDirectDisplayCopyCurrentMetalDevice(_:)`](https://developer.apple.com/documentation/CoreGraphics/CGDirectDisplayCopyCurrentMetalDevice(_:)) function to get the device that drives that display.

## See Also

- [Finding Multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)
  Locate, identify, and choose suitable GPUs for your app.
- [func MTLCopyAllDevices() -> [any MTLDevice]](mtlcopyalldevices().md)
  Returns an array of all the Metal device instances in the system.
- [func MTLCopyAllDevicesWithObserver(handler: MTLDeviceNotificationHandler) -> (devices: [any MTLDevice], observer: NSObject)](mtlcopyalldeviceswithobserver(handler:).md)
  Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [func MTLRemoveDeviceObserver(any NSObjectProtocol)](mtlremovedeviceobserver(_:).md)
  Removes a registered observer of device notifications.
- [func CGDirectDisplayCopyCurrentMetalDevice(_ display: CGDirectDisplayID) -> (any MTLDevice)?](../CoreGraphics/CGDirectDisplayCopyCurrentMetalDevice(_:).md)
  Returns the GPU device instance that’s currently driving a display.
- [typealias MTLDeviceNotificationHandler](mtldevicenotificationhandler.md)
  A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.
- [struct MTLDeviceNotificationName](mtldevicenotificationname.md)
  A notification that represents a change to a GPU device in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/getting-the-gpu-that-drives-a-views-display)*