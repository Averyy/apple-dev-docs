# filterPredicate(forFilteredLanguages:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a font picker filter based on language support.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`languageFilter`](./languagefilter.md) instead.

## Declaration

```swift
class func filterPredicate(forFilteredLanguages filteredLanguages: [String]) -> NSPredicate?
```

```objc
+ (NSPredicate *) filterPredicateForFilteredLanguages:(NSArray<NSString *> *) filteredLanguages;
```

## Return Value

A predicate that is [`true`](../../../Swift/true.md) when at least one of the provided strings is present.

## Discussion

Use this method to construct a predicate for [`filteredLanguagesPredicate`](./filteredlanguagespredicate.md) that restricts the font picker’s list to only include fonts that support the filtered languages. Provide language identifiers in the same format [`CFLocale`](../../../CoreFoundation/cflocale.md) uses.

## Parameters

- `filteredLanguages`: Identifiers for the languages the font picker should include.

## See Also

### Filtering available fonts
- [var includeFaces: Bool](./includefaces.md)
  A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [var filteredTraits: UIFontDescriptor.SymbolicTraits](./filteredtraits.md)
  A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [var filteredLanguagesPredicate: NSPredicate?](./filteredlanguagespredicate.md)
  A predicate to filter fonts based on the languages they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:))*