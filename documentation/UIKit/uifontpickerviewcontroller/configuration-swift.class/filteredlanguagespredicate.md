# filteredLanguagesPredicate

**Framework**: UIKit  
**Kind**: property

A predicate to filter fonts based on the languages they support.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var filteredLanguagesPredicate: NSPredicate? { get set }
```

#### Discussion

By default, the font picker shows all available fonts, regardless of the languages they support. You may prefer to offer only fonts that support certain languages. To restrict the list, set this property to an [`NSPredicate`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_206) defining the logic the font picker should apply to the fonts’ supported languages metadata.

Use language specifiers in the same format doc://com.apple.documentation/documentation/corefoundation/cflocale-rsj uses to specify languages in a filter predicate. You can use [`filterPredicate(forFilteredLanguages:)`](uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:).md) to construct a simple predicate that excludes fonts which don’t support any of a collection of languages you specify.

## See Also

- [var includeFaces: Bool](uifontpickerviewcontroller/configuration-swift.class/includefaces.md)
  A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [var filteredTraits: UIFontDescriptor.SymbolicTraits](uifontpickerviewcontroller/configuration-swift.class/filteredtraits.md)
  A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [class func filterPredicate(forFilteredLanguages: [String]) -> NSPredicate?](uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:).md)
  Creates a font picker filter based on language support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate)*