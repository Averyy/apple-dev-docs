# NSPressureConfiguration

**Framework**: AppKit  
**Kind**: class

An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
class NSPressureConfiguration
```

#### Overview

Use an [`NSPressureConfiguration`](nspressureconfiguration.md) object to configure the behavior and progression of a Force Touch trackpad when it responds to a mouse drag or pressure event sequence. Pressure configurations are assigned to views ([`NSView`](nsview.md)) and gesture recognizers ([`NSGestureRecognizer`](nsgesturerecognizer.md)).

## Topics

### Creating a Pressure Configuration Object
- [init(pressureBehavior: NSEvent.PressureBehavior)](nspressureconfiguration/init(pressurebehavior:).md)
  Initializes a pressure configuration object with a specified pressure behavior.
- [func set()](nspressureconfiguration/set.md)
  Changes the pressure configuration of the trackpad to the initialized pressure configuration.
### Accessing Pressure Configuration Object Properties
- [var pressureBehavior: NSEvent.PressureBehavior](nspressureconfiguration/pressurebehavior.md)
  The pressure behavior of the pressure configuration object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSHapticFeedbackManager](nshapticfeedbackmanager.md)
  An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressureconfiguration)*