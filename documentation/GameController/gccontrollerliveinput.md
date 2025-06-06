# GCControllerLiveInput

**Framework**: Game Controller  
**Kind**: class

The input profile for a controller.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerLiveInput
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Overview

Instances of [`GCControllerLiveInput`](gccontrollerliveinput.md) represent the current input state of a controller. You can save snapshots of the input state and receive callbacks when the input state changes. You can also get the elements of the controller and their current input values from [`GCControllerLiveInput`](gccontrollerliveinput.md) instances.

Use the [`capture()`](gccontrollerliveinput/capture().md) method to save a copy of the current input state. If you want Game Controller to buffer snapshots of the input states for you, use the  [`inputStateQueueDepth`](gcdevicephysicalinput/inputstatequeuedepth.md) property to set the buffer’s queue depth to a value other than `0`. Then use the [`nextInputState()`](gccontrollerliveinput/nextinputstate().md) method to get the snapshots when you’re ready to process input.

## Topics

### Handling device input
- [func nextInputState() -> (any GCControllerInputState & GCDevicePhysicalInputStateDiff)?](gccontrollerliveinput/nextinputstate.md)
  Returns the next device input state from the queue.
- [func capture() -> GCControllerInputState](gccontrollerliveinput/capture.md)
  Returns a snapshot of the physical device inputs.
### Remapping controls
- [var unmapped: GCControllerLiveInput?](gccontrollerliveinput/unmapped.md)
  The live input of a controller without any system-level remapping of the controls.

## Relationships

### Inherits From
- [GCControllerInputState](gccontrollerinputstate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GCDevicePhysicalInput](gcdevicephysicalinput.md)
- [GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var input: GCControllerLiveInput](gccontroller/input.md)
  The input profile for the controller.
- [class GCControllerInputState](gccontrollerinputstate.md)
  A class that represents an input state for gamepads and arcade sticks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerliveinput)*