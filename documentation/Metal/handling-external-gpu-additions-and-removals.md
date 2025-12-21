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

> 💡 **Tip**:  Support external GPUs effectively by setting the `GPUEjectPolicy` key in your app’s `Info.plist` to `“wait”` and appropriately respond to a safe disconnect ([`removalRequested`](mtldevicenotificationname/removalrequested.md)) notification.

##### Set a Gpu Selection Policy

You can control whether Metal prefers to use or avoid external GPUs by configuring the `GPUSelectionPolicy` key in your app’s `Info.plist`. You can assign the key to one of the following string values:

##### Register for External Gpu Notifications

Call the [`MTLCopyAllDevicesWithObserver`](mtlcopyalldeviceswithobserver.md) function to get a list of all the Metal devices available to a system and register an observer that’s called whenever this list changes (or may change due to a safe disconnect request).

To deregister the observer, call the [`MTLRemoveDeviceObserver(_:)`](mtlremovedeviceobserver(_:).md) function.

##### Respond to External Gpu Notifications

Metal notifies your app about the following external GPU events:

Set up a method to respond to the notifications, and pass that method to the `handler` parameter of the [`MTLCopyAllDevicesWithObserver`](mtlcopyalldeviceswithobserver.md) function.

## See Also

- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/handling-external-gpu-additions-and-removals)*