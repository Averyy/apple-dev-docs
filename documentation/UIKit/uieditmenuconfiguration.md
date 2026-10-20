# UIEditMenuConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIEditMenuConfiguration : NSObject
```

#### Overview

You use this object when calling the [`presentEditMenu(with:)`](./uieditmenuinteraction/presenteditmenu%28with%29.md) method of [`UIEditMenuInteraction`](./uieditmenuinteraction.md) to provide the configuration details the interaction’s delegate uses to construct the menu that the interaction displays.

## Topics

### Creating an edit menu configuration
- [convenience init(identifier: AnyHashable?, sourcePoint: CGPoint)](./uieditmenuconfiguration/init%28identifier,sourcepoint%29.md)
  Initializes a new configuration with the source location you specify.
### Getting the configuration identifier
- [var identifier: AnyHashable](./uieditmenuconfiguration/identifier-cjqj.md)
  The unique identifier for this configuration object.
### Configuring the menu
- [var preferredArrowDirection: UIEditMenuArrowDirection](./uieditmenuconfiguration/preferredarrowdirection.md)
  The preferred direction the arrow of the edit menu is pointing.
- [enum UIEditMenuArrowDirection](./uieditmenuarrowdirection.md)
  Constants that describe the direction the arrow of the edit menu is pointing.
- [var sourcePoint: CGPoint](./uieditmenuconfiguration/sourcepoint.md)
  The source location of the interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Edit menus
- [class UIEditMenuInteraction](./uieditmenuinteraction.md)
  An interaction that provides edit operations using a menu.
- [protocol UIEditMenuInteractionDelegate](./uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.
- [protocol UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
  A set of standard methods that apps can adopt to support editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuconfiguration)*