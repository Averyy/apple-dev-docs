# UIMainMenuSystem

**Framework**: UIKit  
**Kind**: class

The main menu system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
class UIMainMenuSystem
```

## Topics

### Accessing the main menu system
- [class var shared: UIMainMenuSystem](uimainmenusystem/shared.md)
  The shared main menu system.
### Configuring a main menu system
- [func setBuildConfiguration(UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)?)](uimainmenusystem/setbuildconfiguration(_:buildhandler:).md)
- [UIMainMenuSystem.Configuration](uimainmenusystem/configuration.md)
  A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.
### Inspecting a configuration of find elements
- [UIMenuSystem.FindElementGroupConfiguration](uimenusystem/findelementgroupconfiguration.md)
  Represents a configuration for find elements, should they be present. You don’t create one of these directly. A configuration is provided as part of a `UIMainMenuSystemConfiguration`.
- [UIMenuSystem.FindElementGroupConfiguration.Style](uimenusystem/findelementgroupconfiguration/style-swift.enum.md)
  Represents a preference for the structure of Find elements in the main menu.

## Relationships

### Inherits From
- [UIMenuSystem](uimenusystem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class UIMenu](uimenu.md)
  A container for grouping related menu elements in an app menu or contextual menu.
- [protocol UIMenuBuilder](uimenubuilder.md)
  An interface for adding and removing menus from a menu system.
- [class UIMenuSystem](uimenusystem.md)
  An object representing a main or contextual menu system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimainmenusystem)*