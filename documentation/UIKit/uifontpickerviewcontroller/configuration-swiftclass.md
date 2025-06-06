# UIFontPickerViewController.Configuration

**Framework**: UIKit  
**Kind**: class

The filters and display settings a font picker view controller uses to set up a font picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class Configuration
```

## Topics

### Customizing the font picker’s appearance
- [var displayUsingSystemFont: Bool](uifontpickerviewcontroller/configuration-swift.class/displayusingsystemfont.md)
  A Boolean value that determines whether to use the system font for all font names in the font picker.
### Filtering available fonts
- [var includeFaces: Bool](uifontpickerviewcontroller/configuration-swift.class/includefaces.md)
  A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [var filteredTraits: UIFontDescriptor.SymbolicTraits](uifontpickerviewcontroller/configuration-swift.class/filteredtraits.md)
  A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [var filteredLanguagesPredicate: NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate.md)
  A predicate to filter fonts based on the languages they support.
- [class func filterPredicate(forFilteredLanguages: [String]) -> NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:).md)
  Creates a font picker filter based on language support.
### Instance Properties
- [var languageFilter: Predicate<[String]>?](uifontpickerviewcontroller/configuration-swift.class/languagefilter.md)

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

- [class UIFontPickerViewController](uifontpickerviewcontroller.md)
  A view controller that manages the interface for selecting a font that the system provides or the user installs.
- [protocol UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)
  A set of optional methods for receiving messages about the user’s interaction with the font picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class)*