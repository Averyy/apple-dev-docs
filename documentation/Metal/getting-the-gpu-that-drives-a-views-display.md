# Getting the GPU that drives a view’s display

**Framework**: Metal  
**Role**: Article

Keep up to date with the optimal device for your display.

## Overview

A user can have multiple external displays connected directly to a Mac or to an external GPU. Each view in your app shows on a single display, and a single GPU drives each display. The display in which your view appears and the GPU that drives the display can change dynamically; therefore, you need to prepare your app to handle these changes. Register for display change notifications, get the device that drives your view’s display, and decide if your app should use that device to present rendered graphics.

### Handle display change notifications

Register for the following notifications so the system can notify your app about specific display changes:

- **[`didChangeScreenNotification`](../AppKit/nswindow/didchangescreennotification.md)**: The system posts this notification when any window, including the window containing your view, moves to a different display.
- **[`didChangeScreenParametersNotification`](../AppKit/nsapplication/didchangescreenparametersnotification.md)**: The system posts this notification when the Mac system’s display configuration changes; for example, when the user connects or disconnects an external display from the system. Another example is when the GPU driving the display changes, such as when system has automatic graphics switching enabled and switches between the discrete and integrated GPUs to drive the display.

When the system posts a display change notification, you can decide if you should get and use a new device.

**Swift**:

```swift
@objc func handleDisplayChanges(notification: NSNotification) {
    // Handle display changes
}

func registerForDisplayChangeNotifications() {
    NotificationCenter.default.addObserver(self,
                                           selector: #selector(handleDisplayChanges(notification:)),
                                           name: NSNotification.Name(rawValue: "NSWindowDidChangeScreenNotification"),
                                           object: nil)
    
    NotificationCenter.default.addObserver(self,
                                           selector: #selector(handleDisplayChanges(notification:)),
                                           name: NSNotification.Name(rawValue: "NSApplicationDidChangeScreenParametersNotification"),
                                           object: nil)
}
```

**Objective-C**:

```objective-c
- (void)handleDisplayChanges:(NSNotification *)notification
{
    // Handle display changes
}

- (void)registerForDisplayChangeNotifications
{
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleDisplayChanges:)
                                                 name:NSWindowDidChangeScreenNotification
                                               object:nil];
    
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleDisplayChanges:)
                                                 name:NSApplicationDidChangeScreenParametersNotification
                                               object:nil];
}
```

To deregister from the previous notifications, call the [`removeObserver(_:name:object:)`](../Foundation/notificationcenter/removeobserver%28_,name,object%29.md) method.

### Identify the device that drives your view’s display

Get the [`CGDirectDisplayID`](../CoreGraphics/cgdirectdisplayid.md) value for the display in which your view currently appears. Then call the [`CGDirectDisplayCopyCurrentMetalDevice(_:)`](../CoreGraphics/cgdirectdisplaycopycurrentmetaldevice%28_%29.md) function to get the device that drives that display.

**Swift**:

```swift
guard let viewDisplayID = mtkView.window?.screen?.deviceDescription[NSDeviceDescriptionKey("NSScreenNumber")] as? CGDirectDisplayID else { return }
let displayDevice = CGDirectDisplayCopyCurrentMetalDevice(viewDisplayID)
```

**Objective-C**:

```objective-c
NSNumber           *screenNumber = _mtkView.window.screen.deviceDescription[@"NSScreenNumber"];
CGDirectDisplayID  viewDisplayID  = [screenNumber unsignedIntValue];
id <MTLDevice>     displayDevice  = CGDirectDisplayCopyCurrentMetalDevice(viewDisplayID);
```

## See Also

### Locating GPUs
- [Finding multiple GPUs on an Intel-based Mac](./finding-multiple-gpus-on-an-intel-based-mac.md)
  Locate, identify, and choose suitable GPUs for your app.
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
- [struct MTLDeviceNotificationName](./mtldevicenotificationname.md)
  A notification that represents a change to a GPU device in the system.
- [MTLCopyAllDevicesWithObserver](./mtlcopyalldeviceswithobserver.md)
  Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/getting-the-gpu-that-drives-a-views-display)*