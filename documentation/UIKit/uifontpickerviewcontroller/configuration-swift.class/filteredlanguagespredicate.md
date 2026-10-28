# filteredLanguagesPredicate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A predicate to filter fonts based on the languages they support.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`languageFilter`](./languagefilter.md) instead.

## Declaration

```swift
@NSCopying
var filteredLanguagesPredicate: NSPredicate? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSPredicate * filteredLanguagesPredicate;
```

## Discussion

By default, the font picker shows all available fonts, regardless of the languages they support. You may prefer to offer only fonts that support certain languages. To restrict the list, set this property to an [NSPredicate](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_206) defining the logic the font picker should apply to the fonts’ supported languages metadata.

Use language specifiers in the same format [`CFLocale`](../../../CoreFoundation/cflocale.md) uses to specify languages in a filter predicate. You can use [`filterPredicate(forFilteredLanguages:)`](./filterpredicate%28forfilteredlanguages%29.md) to construct a simple predicate that excludes fonts which don’t support any of a collection of languages you specify.

## See Also

### Filtering available fonts
- [var includeFaces: Bool](./includefaces.md)
  A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [var filteredTraits: UIFontDescriptor.SymbolicTraits](./filteredtraits.md)
  A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [class func filterPredicate(forFilteredLanguages: [String]) -> NSPredicate?](./filterpredicate%28forfilteredlanguages%29.md)
  Creates a font picker filter based on language support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate)*