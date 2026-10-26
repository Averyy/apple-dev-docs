# GCUIEventTypes

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct GCUIEventTypes
```

```c
enum GCUIEventTypes : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./gcuieventtypes/init%28rawvalue%29.md)
### Type Properties
- [static var gamepad: GCUIEventTypes](./gcuieventtypes/gamepad.md)
- [static var stylus: GCUIEventTypes](./gcuieventtypes/stylus.md)
  A constant that represents events from a stylus.
### Enumeration Cases
- [GCUIEventTypeNone](./gcuieventtypes/gcuieventtypenone.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Getting the event types
- [var handledEventTypes: GCUIEventTypes](./gceventinteraction/handledeventtypes.md)
  The types of game controller events that should be delivered through the Game Controller framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcuieventtypes)*