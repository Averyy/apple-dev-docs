# Multi-GPU Systems

**Framework**: Metal

Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.

#### Overview

Your app can submit work to any or all of the GPUs of a system that supports multiple GPUs. For example, every Mac notebook, such as a MacBook Pro, has an internal GPU, but some have two.

![A system diagram that shows two built-in GPUs within a MacBook Pro.](https://docs-assets.developer.apple.com/published/b022119842cf3a4a9bc64718e4ac3a20/media-4005119%402x.png)

A Mac may have a Thunderbolt connection to an external GPU and its displays.

![A system diagram that shows an external GPU that connects a MacBook Pro to an external display.](https://docs-assets.developer.apple.com/published/b22a3f95645c4220377c91079b7fb6c5/media-4085389%402x.png)

Some systems may have even more complicated arrangements of internal and multiple external GPUs and displays.

![A system diagram that shows an iMac Pro connected to an external display, an external GPU, and another external GPU that’s also connected to two additional external displays.](https://docs-assets.developer.apple.com/published/b505af846a78d0167e779ce702fb7d61/media-4005116%402x.png)

For more information about Mac configurations with GPUs and displays, see [`Assessing Multi-GPU and Multi-Display Setups on an Intel-Based Mac`](assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac.md).

Start by locating all GPUs in a system and identifying their types (see [`Finding Multiple GPUs on an Intel-based Mac`](finding-multiple-gpus-on-an-intel-based-mac.md)). Alternatively, you can locate a specific GPU that’s driving a display (see [`Getting the GPU that Drives a View’s Display`](getting-the-gpu-that-drives-a-views-display.md)).

When selecting a GPU, consider its memory bandwidth and the storage mode options for its memory resources (see [`Adjusting for GPU Memory Bandwidth Tradeoffs`](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)).

For examples of how to use external GPUs in your graphics rendering or compute processing workflows, see the following:

- [`Selecting Device Objects for Graphics Rendering`](selecting-device-objects-for-graphics-rendering.md)
- [`Selecting Device Objects for Compute Processing`](selecting-device-objects-for-compute-processing.md)

For more information about external GPU configurations, see [`Use an external graphics processor with your Mac`](https://developer.apple.comhttps://support.apple.com/kb/HT208544).

> **Note**:  The system may gain or lose an external GPU at any time (see [`Handling External GPU Additions and Removals`](handling-external-gpu-additions-and-removals.md)).

## Topics

### Locating GPUs
- [Finding Multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)
  Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that Drives a View’s Display](getting-the-gpu-that-drives-a-views-display.md)
  Keep up to date with the optimal device for your display.
- [func MTLCopyAllDevices() -> [any MTLDevice]](mtlcopyalldevices().md)
  Returns an array of all the Metal device instances in the system.
- [func MTLCopyAllDevicesWithObserver(handler: (any MTLDevice, MTLDeviceNotificationName) -> Void) -> (devices: [any MTLDevice], observer: NSObject)](mtlcopyalldeviceswithobserver(handler:).md)
  Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [func MTLRemoveDeviceObserver(any NSObjectProtocol)](mtlremovedeviceobserver(_:).md)
  Removes a registered observer of device notifications.
- [func CGDirectDisplayCopyCurrentMetalDevice(_ display: CGDirectDisplayID) -> (any MTLDevice)?](../CoreGraphics/CGDirectDisplayCopyCurrentMetalDevice(_:).md)
  Returns the GPU device instance that’s currently driving a display.
- [typealias MTLDeviceNotificationHandler](mtldevicenotificationhandler.md)
  A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.
- [struct MTLDeviceNotificationName](mtldevicenotificationname.md)
  A notification that represents a change to a GPU device in the system.
### Selecting GPUs
- [Adjusting for GPU Memory Bandwidth Tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
  Choose a suitable GPU and memory storage mode for tasks based on that GPU’s memory bandwidth on a Mac.
- [Assessing Multi-GPU and Multi-Display Setups on an Intel-Based Mac](assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac.md)
  Learn the possible GPU and display configurations for a Mac and their limitations.
- [Selecting Device Objects for Graphics Rendering](selecting-device-objects-for-graphics-rendering.md)
  Switch dynamically between multiple GPUs to efficiently render to a display.
- [Selecting Device Objects for Compute Processing](selecting-device-objects-for-compute-processing.md)
  Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.
### Working with External GPUs
- [Handling External GPU Additions and Removals](handling-external-gpu-additions-and-removals.md)
  Register and respond to external GPU notifications that a person initiates.
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.

## See Also

- [Getting the Default GPU](getting-the-default-gpu.md)
  Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?](mtlcreatesystemdefaultdevice().md)
  Returns the device instance Metal selects as the default.
- [protocol MTLDevice](mtldevice.md)
  The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/multi-gpu-systems)*