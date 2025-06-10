# AXBrailleTable

**Framework**: Accessibility  
**Kind**: class

A rule for translating print text to Braille, and back-translating Braille to print text.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class AXBrailleTable
```

## Topics

### Initializers
- [init?(identifier: String)](axbrailletable/init(identifier:).md)
  Returns nil if there is no table with the given identifier.
### Instance Properties
- [var identifier: String](axbrailletable/identifier.md)
  A unique string that identifies this table.
- [var isEightDot: Bool](axbrailletable/iseightdot.md)
  Returns true if this table makes use of eight dots as opposed to six dots.
- [var language: Locale.Language](axbrailletable/language-3stsd.md)
- [var locales: Set<Locale>](axbrailletable/locales.md)
  All locales this table supports.
- [var localizedName: String](axbrailletable/localizedname.md)
  The localized name of this table for user display.
- [var localizedProviderName: String](axbrailletable/localizedprovidername.md)
  The localized name of the provider of this table for user display.
- [var providerIdentifier: String](axbrailletable/provideridentifier.md)
  The identifier of the provider of this table.
### Type Methods
- [class func defaultTable(for: Locale) -> AXBrailleTable?](axbrailletable/defaulttable(for:).md)
  The default table that provides translations for the given locale’s language. Returns nil if there is none.
- [class func languageAgnosticTables() -> Set<AXBrailleTable>](axbrailletable/languageagnostictables.md)
  All tables that are not specific to any language.
- [class func supportedLocales() -> Set<Locale>](axbrailletable/supportedlocales.md)
  All locales supported by existing tables.
- [class func tables(for: Locale) -> Set<AXBrailleTable>](axbrailletable/tables(for:).md)
  All tables that provide translations for the given locale’s language.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbrailletable)*