# NSOrthography

**Framework**: Foundation  
**Kind**: class

A description of the linguistic content of natural language text, typically used for spelling and grammar checking.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSOrthography
```

#### Overview

Use [`NSOrthography`](nsorthography.md) objects to describe the linguistic content of a piece of text, including which scripts the text contains, a dominant language (and possibly other languages) for each script, and a dominant script and language for the text as a whole.

Scripts are uniformly described by four-letter ISO 15924 script codes, such as `"Latn"`, `"Grek"`, and `"Cyrl"`. The supertags `"Jpan"` and `"Kore"` are typically used for Japanese and Korean text, and `"Hans"` and `"Hant"` are typically used for Chinese text. The tag `"Zyyy"` is used if a specific script cannot be identified. See [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for more information.

Languages are uniformly described by BCP-47 tags (preferably in canonical form). The tag `"und"` is used if a specific language cannot be determined.

You typically work with orthography objects returned from methods and properties for classes like [`NSLinguisticTagger`](nslinguistictagger.md) and [`NSSpellChecker`](https://developer.apple.com/documentation/AppKit/NSSpellChecker).

##### Subclassing Notes

Subclasses must override the [`dominantScript`](nsorthography/dominantscript.md) and [`languageMap`](nsorthography/languagemap.md) properties. These properties are set using [`init(dominantScript:languageMap:)`](nsorthography/init(dominantscript:languagemap:).md) or [`orthographyWithDominantScript:languageMap:`](nsorthography/orthographywithdominantscript:languagemap:.md) in Objective-C.

## Topics

### Creating Orthography Objects
- [class func defaultOrthography(forLanguage: String) -> Self](nsorthography/defaultorthography(forlanguage:).md)
  Creates and returns an orthography object with the default language map for the specified language.
- [init(dominantScript: String, languageMap: [String : [String]])](nsorthography/init(dominantscript:languagemap:).md)
  Creates an orthography object with the specified dominant script and language map.
### Determining Correspondences Between Languages and Scripts
- [var languageMap: [String : [String]]](nsorthography/languagemap.md)
  A dictionary that maps script tags to arrays of language tags.
- [var dominantLanguage: String](nsorthography/dominantlanguage.md)
  The first language in the list of languages for the dominant script.
- [var dominantScript: String](nsorthography/dominantscript.md)
  The dominant script for the text.
- [func dominantLanguage(forScript: String) -> String?](nsorthography/dominantlanguage(forscript:).md)
  Returns the dominant language for the specified script.
- [func languages(forScript: String) -> [String]?](nsorthography/languages(forscript:).md)
  Returns the list of languages for the specified script.
- [var allScripts: [String]](nsorthography/allscripts.md)
  The scripts appearing as keys in the language map.
- [var allLanguages: [String]](nsorthography/alllanguages.md)
  The languages appearing in values of the language map.
### Initializers
- [init?(coder: NSCoder)](nsorthography/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [func NSLocalizedString(String, tableName: String?, bundle: Bundle, value: String, comment: String) -> String](nslocalizedstring(_:tablename:bundle:value:comment:).md)
  Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.
- [protocol CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md)
  A type that provides an out-of-process localizable description.
- [struct URLResource](urlresource.md)
  A resource located at a particular file URL within a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorthography)*