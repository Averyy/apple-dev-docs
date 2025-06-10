# UIMainMenuSystem.Configuration

**Framework**: UIKit  
**Kind**: class

A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class Configuration
```

## Topics

### Instance Properties
- [var documentPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/documentpreference.md)
  Specifies a preference for document elements in the main menu.
- [var findingConfiguration: UIMenuSystem.FindElementGroupConfiguration](uimainmenusystem/configuration/findingconfiguration.md)
  Configuration for the find elements should they be present in the main menu.
- [var findingPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/findingpreference.md)
  Specifies a preference for finding elements in the main menu.
- [var inspectorPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/inspectorpreference.md)
  Specifies a preference for inspector elements in the main menu.
- [var newScenePreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/newscenepreference.md)
  Specifies a preference for new scene elements in the main menu.
- [var printingPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/printingpreference.md)
  Specifies a preference for printing elements in the main menu.
- [var sidebarPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/sidebarpreference.md)
  Specifies a preference for sidebar elements in the main menu.
- [var textFormattingPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/textformattingpreference.md)
  Specifies a preference for text formatting elements in the main menu.
- [var toolbarPreference: UIMenuSystem.ElementGroupPreference](uimainmenusystem/configuration/toolbarpreference.md)
  Specifies a preference for toolbar elements in the main menu.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setBuildConfiguration(UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)?)](uimainmenusystem/setbuildconfiguration(_:buildhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimainmenusystem/configuration)*