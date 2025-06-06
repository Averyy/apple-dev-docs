# filterPredicate(forFilteredLanguages:)

**Framework**: UIKit  
**Kind**: method

Creates a font picker filter based on language support.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func filterPredicate(forFilteredLanguages filteredLanguages: [String]) -> NSPredicate?
```

#### Return Value

A predicate that is [`true`](https://developer.apple.com/documentation/swift/true) when at least one of the provided strings is present.

#### Discussion

Use this method to construct a predicate for [`filteredLanguagesPredicate`](uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate.md) that restricts the font picker’s list to only include fonts that support the filtered languages. Provide language identifiers in the same format doc://com.apple.documentation/documentation/corefoundation/cflocale-rsj uses.

## Parameters

- `filteredLanguages`: Identifiers for the languages the font picker should include.

## See Also

- [var includeFaces: Bool](uifontpickerviewcontroller/configuration-swift.class/includefaces.md)
  A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [var filteredTraits: UIFontDescriptor.SymbolicTraits](uifontpickerviewcontroller/configuration-swift.class/filteredtraits.md)
  A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [var filteredLanguagesPredicate: NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate.md)
  A predicate to filter fonts based on the languages they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:))*