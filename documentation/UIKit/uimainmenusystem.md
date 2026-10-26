# UIMainMenuSystem

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIMainMenuSystem : UIMenuSystem
```

## Topics

### Accessing the main menu system
- [class var shared: UIMainMenuSystem](./uimainmenusystem/shared.md)
  The shared main menu system.
### Configuring a main menu system
- [func setBuildConfiguration(UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)?)](./uimainmenusystem/setbuildconfiguration%28_,buildhandler%29.md)
- [UIMainMenuSystem.Configuration](./uimainmenusystem/configuration.md)
  A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.
- [- setBuildConfiguration:buildHandler:](./uimainmenusystem/setbuildconfiguration_buildhandler_.md)
  Specifies that the main menu system should be built using the specified configuration. A build handler can be optionally provided, which the main menu system will use instead of calling `-buildMenuWithBuilder:`. Setting this will invalidate and rebuild the main menu system. Ideally it should be set once, and as early as possible, preferably in `-application:didFinishLaunchingWithOptions:`. Subsequent rebuilds of the main menu system will continue to use this `configuration` and `buildHandler`. It is a developer error to set the `configuration` while the main menu system is building. Doing so will assert.
### Inspecting a configuration of find elements
- [UIMenuSystem.FindElementGroupConfiguration](./uimenusystem/findelementgroupconfiguration.md)
  Represents a configuration for find elements, should they be present. You don’t create one of these directly. A configuration is provided as part of a `UIMainMenuSystemConfiguration`.
- [UIMenuSystem.FindElementGroupConfiguration.Style](./uimenusystem/findelementgroupconfiguration/style-swift.enum.md)
  Represents a preference for the structure of Find elements in the main menu.

## Relationships

### Inherits From
- [UIMenuSystem](./uimenusystem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### App menus
- [class UIMenu](./uimenu.md)
  A container for grouping related menu elements in an app menu or contextual menu.
- [protocol UIMenuBuilder](./uimenubuilder.md)
  An interface for adding and removing menus from a menu system.
- [class UIMenuSystem](./uimenusystem.md)
  An object representing a main or contextual menu system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimainmenusystem)*