# UIMainMenuSystem.Configuration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
class Configuration
```

```objc
@interface UIMainMenuSystemConfiguration : NSObject
```

## Topics

### Instance Properties
- [var documentPreference: UIMenuSystem.ElementGroupPreference](./configuration/documentpreference.md)
  Specifies a preference for document elements in the main menu.
- [var findingConfiguration: UIMenuSystem.FindElementGroupConfiguration](./configuration/findingconfiguration.md)
  Configuration for the find elements should they be present in the main menu.
- [var findingPreference: UIMenuSystem.ElementGroupPreference](./configuration/findingpreference.md)
  Specifies a preference for finding elements in the main menu.
- [var inspectorPreference: UIMenuSystem.ElementGroupPreference](./configuration/inspectorpreference.md)
  Specifies a preference for inspector elements in the main menu.
- [var newScenePreference: UIMenuSystem.ElementGroupPreference](./configuration/newscenepreference.md)
  Specifies a preference for new scene elements in the main menu.
- [var printingPreference: UIMenuSystem.ElementGroupPreference](./configuration/printingpreference.md)
  Specifies a preference for printing elements in the main menu.
- [var sidebarPreference: UIMenuSystem.ElementGroupPreference](./configuration/sidebarpreference.md)
  Specifies a preference for sidebar elements in the main menu.
- [var textFormattingPreference: UIMenuSystem.ElementGroupPreference](./configuration/textformattingpreference.md)
  Specifies a preference for text formatting elements in the main menu.
- [var toolbarPreference: UIMenuSystem.ElementGroupPreference](./configuration/toolbarpreference.md)
  Specifies a preference for toolbar elements in the main menu.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Configuring a main menu system
- [func setBuildConfiguration(UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)?)](./setbuildconfiguration%28_,buildhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimainmenusystem/configuration)*