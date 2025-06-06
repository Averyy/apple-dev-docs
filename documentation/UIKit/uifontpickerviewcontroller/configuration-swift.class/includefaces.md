# includeFaces

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var includeFaces: Bool { get set }
```

#### Discussion

By default, the font picker only lists font families, like Times New Roman or Helvetica. Set [`includeFaces`](uifontpickerviewcontroller/configuration-swift.class/includefaces.md) to [`true`](https://developer.apple.com/documentation/swift/true) so the user can select a specific font face, such as Times New Roman Bold or Helvetica Light Oblique.

## See Also

- [var filteredTraits: UIFontDescriptor.SymbolicTraits](uifontpickerviewcontroller/configuration-swift.class/filteredtraits.md)
  A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [var filteredLanguagesPredicate: NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate.md)
  A predicate to filter fonts based on the languages they support.
- [class func filterPredicate(forFilteredLanguages: [String]) -> NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:).md)
  Creates a font picker filter based on language support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/includefaces)*