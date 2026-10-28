# GCControllerInputState

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

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

```objc
@interface GCControllerInputState : NSObject
```

## Overview

This class implements the [`GCDevicePhysicalInputState`](./gcdevicephysicalinputstate.md) protocol for gamepads and arcade sticks. Instances of this class represent the state of the controller’s inputs at a moment in time, which can be the current time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [GCControllerLiveInput](./gccontrollerliveinput.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [GCDevicePhysicalInputState](./gcdevicephysicalinputstate.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing controller input
- [var input: GCControllerLiveInput](./gccontroller/input.md)
  The input profile for the controller.
- [class GCControllerLiveInput](./gccontrollerliveinput.md)
  The input profile for a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerinputstate)*