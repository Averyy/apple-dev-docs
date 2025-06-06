# GCDevicePhysicalInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties and methods for objects that represent the input profile of a device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCDevicePhysicalInput : GCDevicePhysicalInputState
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Overview

You can safely call this protocol’s methods and access its properties from any thread, but not from multiple, concurrent threads.

## Topics

### Getting the device
- [var device: (any GCDevice)?](gcdevicephysicalinput/device.md)
  The device that the physical input represents.
### Handling device input
- [func nextInputState() -> (any GCDevicePhysicalInputState & GCDevicePhysicalInputStateDiff)?](gcdevicephysicalinput/nextinputstate.md)
  Returns the next input state from the queue.
- [var inputStateAvailableHandler: ((any GCDevicePhysicalInput) -> Void)?](gcdevicephysicalinput/inputstateavailablehandler.md)
  The block that the profile calls when Game Controller adds an input state to the queue.
- [var inputStateQueueDepth: Int](gcdevicephysicalinput/inputstatequeuedepth.md)
  The maximum number of input values that the queue stores.
- [func capture() -> any GCDevicePhysicalInputState](gcdevicephysicalinput/capture.md)
  Returns a snapshot of the physical device inputs.
- [var elementValueDidChangeHandler: ((any GCDevicePhysicalInput, any GCPhysicalInputElement) -> Void)?](gcdevicephysicalinput/elementvaluedidchangehandler.md)
  A block that the profile calls when an element’s value changes.
### Changing the callback dispatch queue
- [var queue: dispatch_queue_t?](gcdevicephysicalinput/queue.md)
  The dispatch queue that the system uses for callbacks.

## Relationships

### Inherits From
- [GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [GCControllerLiveInput](gccontrollerliveinput.md)
- [GCRacingWheelInput](gcracingwheelinput.md)

## See Also

- [Handling input events](handling-input-events.md)
  Receive controller input using either polling or callbacks.
- [protocol GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
  The common properties for physical devices with elements.
- [protocol GCDevicePhysicalInputStateDiff](gcdevicephysicalinputstatediff.md)
  The common functions for objects that contain the differences between a current and previous input state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput)*