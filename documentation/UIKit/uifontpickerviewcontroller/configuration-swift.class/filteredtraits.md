# filteredTraits

**Framework**: UIKit  
**Kind**: property

A predicate to filter fonts based on their traits, like bold, italic, or monospace.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var filteredTraits: UIFontDescriptor.SymbolicTraits { get set }
```

## See Also

- [var includeFaces: Bool](uifontpickerviewcontroller/configuration-swift.class/includefaces.md)
  A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [var filteredLanguagesPredicate: NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate.md)
  A predicate to filter fonts based on the languages they support.
- [class func filterPredicate(forFilteredLanguages: [String]) -> NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:).md)
  Creates a font picker filter based on language support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredtraits)*