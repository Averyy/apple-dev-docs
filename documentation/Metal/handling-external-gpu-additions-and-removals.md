# Handling external GPU additions and removals

**Framework**: Metal

Register and respond to external GPU notifications that a person initiates.

#### Overview

A person can connect or disconnect external GPUs from a Mac at any time. The following sequence of events occurs when a person properly adds and removes an external GPU from the system:

1. A person physically connects an external GPU, macOS adds it to the system, and Metal makes the GPU available to your app.
2. While the system has one or more external GPUs, macOS presents a menu bar icon that allows a person to safely disconnect any external GPU.
3. A person safely disconnects an external GPU.
4. Metal notifies your app of the request, and your app migrates all current and future work off of the external GPU.
5. After all apps (including yours) have stopped using the external GPU, macOS notifies the user that it’s safe to disconnect the GPU.
6. The system removes the external GPU so a person can physically disconnect the GPU from the Mac.

Your app can support external GPUs effectively by responding to these events appropriately.

> ⚠️ **Warning**:  A person can disconnect an external GPU from a Mac at any time, without requesting or following a safe disconnect procedure. Prepare your app for this possibility and take actions in response to an unexpected removal.

##### Set a Gpu Eject Policy

You can control how your app responds to a safe disconnect request for an external GPU by configuring the `GPUEjectPolicy` key in your app’s `Info.plist`. You can assign the key to one of the following string values:

- **`"wait"`**: Tells the system your app manually responds to the safe disconnect request. Your app needs to register and respond to the [`removalRequested`](mtldevicenotificationname/removalrequested.md) notification Metal posts. The system waits for your app to remove all references to the external GPU before notifying a person that it’s safe to disconnect the GPU.
- **`“relaunch”`**: Allow macOS to quit and relaunch your app with another GPU. Your app can save any state before it quits by implementing the [`application(_:willEncodeRestorableState:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/application(_:willEncodeRestorableState:)) method, and restore it at launch by implementing the [`application(_:didDecodeRestorableState:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/application(_:didDecodeRestorableState:)) method.
- **`“kill”`**: Allows macOS to force your app to quit.

> 💡 **Tip**:  Support external GPUs effectively by setting the `GPUEjectPolicy` key in your app’s `Info.plist` to `“wait”` and appropriately respond to a safe disconnect ([`removalRequested`](mtldevicenotificationname/removalrequested.md)) notification.

##### Set a Gpu Selection Policy

You can control whether Metal prefers to use or avoid external GPUs by configuring the `GPUSelectionPolicy` key in your app’s `Info.plist`. You can assign the key to one of the following string values:

- **`“avoidRemovable”`**: Metal tries to avoid creating contexts on external GPUs. For legacy OpenGL apps, OpenGL also tries to avoid creating contexts for external GPUs. Set this option only if your app doesn’t run well on an external GPU.
- **`“preferRemovable”`**: If external GPUs are visible to the system, Metal prefers them over other GPUs. Similarly, for legacy OpenGL apps, OpenGL also prefers to create contexts for the external GPU.

##### Register for External Gpu Notifications

Call the [`MTLCopyAllDevicesWithObserver`](mtlcopyalldeviceswithobserver.md) function to get a list of all the Metal devices available to a system and register an observer that’s called whenever this list changes (or may change due to a safe disconnect request).

**Swift**:

```swift
let devicesWithObserver = MTLCopyAllDevicesWithObserver(handler: { (device, name) in
    self.handleExternalGPUEvents(device: device, notification: name)
})
deviceList = devicesWithObserver.devices
deviceObserver = devicesWithObserver.observer
```

**Objective-C**:

```objective-c
id <NSObject> deviceObserver  = nil;
NSArray<id<MTLDevice>> *deviceList = nil;
deviceList = MTLCopyAllDevicesWithObserver(&deviceObserver,
                                           ^(id<MTLDevice> device, MTLDeviceNotificationName name) {
                                               [self handleExternalGPUEventsForDevice:device notification:name];
                                           });
_deviceObserver = deviceObserver;
_deviceList = deviceList;
```

To deregister the observer, call the [`MTLRemoveDeviceObserver(_:)`](mtlremovedeviceobserver(_:).md) function.

##### Respond to External Gpu Notifications

Metal notifies your app about the following external GPU events:

- **[`wasAdded`](mtldevicenotificationname/wasadded.md)**: Metal posts this notification when macOS adds an external GPU to the system. Evaluate the updated list of devices and consider using the new addition.
- **[`removalRequested`](mtldevicenotificationname/removalrequested.md)**: Metal posts this notification when the user initiates a safe disconnect request for an external GPU. Your app has approximately one second to migrate work off the device and remove all references to it. If your app fails to do so, macOS notifies the user that your app is blocking the safe disconnect request.
- **[`wasRemoved`](mtldevicenotificationname/wasremoved.md)**: Metal posts this notification when macOS removes an external GPU from the system and your app still has references to that device. If the user safely disconnected an external GPU, Metal posts this notification after it posts a [`removalRequested`](mtldevicenotificationname/removalrequested.md) notification. If the user unexpectedly disconnected an external GPU, Metal posts this notification without first posting a [`removalRequested`](mtldevicenotificationname/removalrequested.md) notification. After macOS removes an external GPU, Metal completes any command buffers queued for the device with an error, and any new API calls that reference the device fail with an error.

Set up a method to respond to the notifications, and pass that method to the `handler` parameter of the [`MTLCopyAllDevicesWithObserver`](mtlcopyalldeviceswithobserver.md) function.

**Swift**:

```swift
func handleExternalGPUEvents(device: MTLDevice, notification: MTLDeviceNotificationName) {
    switch notification {
    case .wasAdded:
        // Handle addition
        break
    case .removalRequested:
        // Handle safe disconnect
        break
    case .wasRemoved:
        // Handle removal
        break
    default:
        break
    }
}
```

**Objective-C**:

```objective-c
- (void)handleExternalGPUEventsForDevice:(id<MTLDevice>)device notification:(MTLDeviceNotificationName)notification
{
    if (notification == MTLDeviceWasAddedNotification) {  }
    else if (notification == MTLDeviceRemovalRequestedNotification) {  }
    else if (notification == MTLDeviceWasRemovedNotification) {  }
}
```

## See Also

- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/handling-external-gpu-additions-and-removals)*