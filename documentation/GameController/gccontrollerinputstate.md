# GCControllerInputState

**Framework**: Game Controller  
**Kind**: class

A class that represents an input state for gamepads and arcade sticks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerInputState
```

#### Overview

This class implements the [`GCDevicePhysicalInputState`](gcdevicephysicalinputstate.md) protocol for gamepads and arcade sticks. Instances of this class represent the state of the controller’s inputs at a moment in time, which can be the current time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GCControllerLiveInput](gccontrollerliveinput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var input: GCControllerLiveInput](gccontroller/input.md)
  The input profile for the controller.
- [class GCControllerLiveInput](gccontrollerliveinput.md)
  The input profile for a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerinputstate)*