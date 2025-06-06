# UIEditMenuConfiguration

**Framework**: UIKit  
**Kind**: class

An object containing the configuration details for the menu your app presents in response to an edit menu interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIEditMenuConfiguration
```

#### Overview

You use this object when calling the [`presentEditMenu(with:)`](uieditmenuinteraction/presenteditmenu(with:).md) method of [`UIEditMenuInteraction`](uieditmenuinteraction.md) to provide the configuration details the interaction’s delegate uses to construct the menu that the interaction displays.

## Topics

### Creating an edit menu configuration
- [convenience init(identifier: AnyHashable?, sourcePoint: CGPoint)](uieditmenuconfiguration/init(identifier:sourcepoint:).md)
  Initializes a new configuration with the source location you specify.
### Getting the configuration identifier
- [var identifier: AnyHashable](uieditmenuconfiguration/identifier-cjqj.md)
  The unique identifier for this configuration object.
### Configuring the menu
- [var preferredArrowDirection: UIEditMenuArrowDirection](uieditmenuconfiguration/preferredarrowdirection.md)
  The preferred direction the arrow of the edit menu is pointing.
- [enum UIEditMenuArrowDirection](uieditmenuarrowdirection.md)
  Constants that describe the direction the arrow of the edit menu is pointing.
- [var sourcePoint: CGPoint](uieditmenuconfiguration/sourcepoint.md)
  The source location of the interaction.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIEditMenuInteraction](uieditmenuinteraction.md)
  An interaction that provides edit operations using a menu.
- [protocol UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.
- [protocol UIResponderStandardEditActions](uiresponderstandardeditactions.md)
  A set of standard methods that apps can adopt to support editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuconfiguration)*