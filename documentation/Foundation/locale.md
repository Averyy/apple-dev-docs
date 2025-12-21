# Locale

**Framework**: Foundation  
**Kind**: struct

Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Locale
```

#### Overview

[`Locale`](locale.md) encapsulates information about linguistic, cultural, and technological conventions and standards. Examples of information encapsulated by a locale include the symbol used for the decimal separator in numbers and the formatting conventions for dates and times.

Apps use locales to provide, format, and interpret information about and according to the user’s customs and preferences. Data formatting APIs commonly make use of locales to present data in a locale-appropriate way.

You can create a [`Locale`](locale.md) from a common identifier like `en-US`, or by specifying its components. More commonly, you access the current system locale with the [`current`](locale/current.md) or [`autoupdatingCurrent`](locale/autoupdatingcurrent.md) static variables.

##### Working with Locale Components

A [`Locale`](locale.md) exposes its various traits — the appropriate measurement system, currency symbols, date and time conventions, and more — as strongly-typed properties like [`currency`](locale/currency-swift.property.md), `numberingSystem`, and `firstDayOfWeek`.

In addition, the [`language`](locale/language-swift.property.md) property allows you examine traits of languages, through the [`Locale.Language`](locale/language-swift.struct.md) type, in contast with [`NSLocale`](nslocale.md), where [`languageCode`](nslocale/languagecode.md) is just a string identifier. You can use a locale’s language to compare whether two locales use the same language, or if one language is a parent of another.

The following example creates a [`Locale`](locale.md) from the identifier `zh-CN`, for Chinese. It then accesses this locale’s [`language`](locale/language-swift.property.md) to get the language’s [`script`](locale/language-swift.struct/script.md), and uses a US English locale to get a localized string describing the script: “Simplified Han”. With the locale `zh-Hant-CN`, for Traditional Chinese, the script would be “Traditional Han” instead.

```swift
let zhCN = Locale(identifier: "zh-CN")
if let script = zhCN.language.script {
    let enUS = Locale(identifier: "en-US")
    let localizedScript = enUS.localizedString(forScript: script) // "Simplified Han"
}
```

##### Creating Custom Locales From Components

You can create a custom locale by creating a [`Locale`](locale.md) instance from a customized [`Locale.Components`](locale/components.md). Do this when you want to tweak specific aspects of a locale. The following example creates a locale that uses language conventions of British English (language region `GB`), but otherwise uses US conventions for things like currency and measurement.

```swift
var components = Locale.Components(languageCode: "en", languageRegion: "GB")
components.region = Locale.Region("US")
let en_GB_US = Locale(components: components)
```

Creating a custom locale like this isn’t necessarily common in apps, but can be useful in unit testing your app’s localizations.

## Topics

### Creating a locale by identifier
- [init(identifier: String)](locale/init(identifier:).md)
  Creates a locale with the specified identifier.
### Creating a locale by components
- [init(components: Locale.Components)](locale/init(components:).md)
  Creates a locale from the given components.
- [Locale.Components](locale/components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](locale/init(languagecode:script:languageregion:).md)
  Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents: Locale.Language.Components)](locale/init(languagecomponents:).md)
  Creates a locale from the given language components.
- [Locale.Language.Components](locale/language-swift.struct/components.md)
  A type that identifies a language by its various components.
### Getting the user’s locale
- [static var autoupdatingCurrent: Locale](locale/autoupdatingcurrent.md)
  A locale which tracks the user’s current preferences.
- [static var current: Locale](locale/current.md)
  A locale representing the user’s region settings at the time the property is read.
### Getting known identifiers and codes
- [static var availableIdentifiers: [String]](locale/availableidentifiers.md)
  A list of available identifiers.
- [static var isoRegionCodes: [String]](locale/isoregioncodes.md)
  A list of available region codes.
- [static var isoLanguageCodes: [String]](locale/isolanguagecodes.md)
  A list of available language codes.
- [static var isoCurrencyCodes: [String]](locale/isocurrencycodes.md)
  A list of available currency codes.
- [static var commonISOCurrencyCodes: [String]](locale/commonisocurrencycodes.md)
  A list of common currency codes.
### Converting between identifiers
- [static func canonicalIdentifier(from: String) -> String](locale/canonicalidentifier(from:).md)
  Returns a canonical identifier from the given string.
- [static func components(fromIdentifier: String) -> [String : String]](locale/components(fromidentifier:).md)
  Returns a dictionary that splits an identifier into its component pieces.
- [static func identifier(fromComponents: [String : String]) -> String](locale/identifier(fromcomponents:).md)
  Constructs an identifier from a dictionary of components.
- [static func identifier(Locale.IdentifierType, from: String) -> String](locale/identifier(_:from:).md)
  Returns the identifier conforming to the specified standard for the specified string.
- [Locale.IdentifierType](locale/identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [static func canonicalLanguageIdentifier(from: String) -> String](locale/canonicallanguageidentifier(from:).md)
  Returns a canonical language identifier from the given string.
- [static func identifier(fromWindowsLocaleCode: Int) -> String?](locale/identifier(fromwindowslocalecode:).md)
  Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [static func windowsLocaleCode(fromIdentifier: String) -> Int?](locale/windowslocalecode(fromidentifier:).md)
  Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.
### Getting locale components
- [Locale.Components](locale/components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
### Getting language components
- [var language: Locale.Language](locale/language-swift.property.md)
  The language of a locale.
- [Locale.Language](locale/language-swift.struct.md)
  A type that represents a language, as used in a locale.
### Getting date and time components
- [var firstDayOfWeek: Locale.Weekday](locale/firstdayofweek.md)
  The first day of the week as represented by this locale.
- [Locale.Weekday](locale/weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [var hourCycle: Locale.HourCycle](locale/hourcycle-swift.property.md)
  The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [Locale.HourCycle](locale/hourcycle-swift.enum.md)
  A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [var timeZone: TimeZone?](locale/timezone.md)
  The time zone associated with the locale, if any.
### Getting measurement and counting components
- [var currency: Locale.Currency?](locale/currency-swift.property.md)
  The currency used by the locale.
- [Locale.Currency](locale/currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem](locale/measurementsystem-swift.property.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](locale/measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](locale/numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](locale/availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.
- [Locale.NumberingSystem](locale/numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.
### Getting region components
- [var region: Locale.Region?](locale/region-swift.property.md)
  The region used by the locale.
- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](locale/subdivision-swift.property.md)
  The optional subdivision of the region used by this locale.
- [Locale.Subdivision](locale/subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [var variant: Locale.Variant?](locale/variant-swift.property.md)
  An optional variant used by the locale.
- [Locale.Variant](locale/variant-swift.struct.md)
  A type that represents a locale’s languate variant.
### Getting ordering components
- [var collation: Locale.Collation](locale/collation-swift.property.md)
  The string sort order of the locale.
- [Locale.Collation](locale/collation-swift.struct.md)
  A type that represents the string sort order used by the locale.
### Getting information about a locale
- [var identifier: String](locale/identifier.md)
  The identifier of the locale.
- [func identifier(Locale.IdentifierType) -> String](locale/identifier(_:).md)
  Returns the locale identifier, in the specified standard format.
- [Locale.IdentifierType](locale/identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [var calendar: Calendar](locale/calendar.md)
  The calendar for the locale, or the Gregorian calendar as a fallback.
- [var regionCode: String?](locale/regioncode.md)
  The region code of the locale, or `nil` if it has none.
- [var languageCode: String?](locale/languagecode-swift.property.md)
  The language code of the locale, or `nil` if has none.
- [var scriptCode: String?](locale/scriptcode.md)
  The script code of the locale, or `nil` if has none.
- [var variantCode: String?](locale/variantcode.md)
  The variant code for the locale, or `nil` if it has none.
- [var exemplarCharacterSet: CharacterSet?](locale/exemplarcharacterset.md)
  The exemplar character set for the locale, or `nil` if has none.
- [var collationIdentifier: String?](locale/collationidentifier.md)
  The collation identifier for the locale, or `nil` if it has none.
- [var collatorIdentifier: String?](locale/collatoridentifier.md)
  The collator identifier of the locale.
- [var usesMetricSystem: Bool](locale/usesmetricsystem.md)
  A Boolean that is true if the locale uses the metric system.
- [var decimalSeparator: String?](locale/decimalseparator.md)
  The decimal separator of the locale.
- [var groupingSeparator: String?](locale/groupingseparator.md)
  The grouping separator of the locale.
- [var currencyCode: String?](locale/currencycode.md)
  The currency code of the locale.
- [var currencySymbol: String?](locale/currencysymbol.md)
  The currency symbol of the locale.
- [var quotationBeginDelimiter: String?](locale/quotationbegindelimiter.md)
  The quotation begin delimiter of the locale.
- [var quotationEndDelimiter: String?](locale/quotationenddelimiter.md)
  The quotation end delimiter of the locale.
- [var alternateQuotationBeginDelimiter: String?](locale/alternatequotationbegindelimiter.md)
  The alternate quotation begin delimiter of the locale.
- [var alternateQuotationEndDelimiter: String?](locale/alternatequotationenddelimiter.md)
  The alternate quotation end delimiter of the locale.
### Getting display information about a locale
- [func localizedString(for: Calendar.Identifier) -> String?](locale/localizedstring(for:).md)
  Returns a localized string for a specified calendar.
- [func localizedString(forCollationIdentifier: String) -> String?](locale/localizedstring(forcollationidentifier:).md)
  Returns a localized string for a specified ICU collation identifier.
- [func localizedString(forCollatorIdentifier: String) -> String?](locale/localizedstring(forcollatoridentifier:).md)
  Returns a localized string for a specified ICU collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](locale/localizedstring(forcurrencycode:).md)
  Returns a localized string for a specified ISO 4217 currency code.
- [func localizedString(forIdentifier: String) -> String?](locale/localizedstring(foridentifier:).md)
  Returns a localized string for a specified locale identifier.
- [func localizedString(forLanguageCode: String) -> String?](locale/localizedstring(forlanguagecode:).md)
  Returns a localized string for a specified language code.
- [func localizedString(forRegionCode: String) -> String?](locale/localizedstring(forregioncode:).md)
  Returns a localized string for a specified region code.
- [func localizedString(forScriptCode: String) -> String?](locale/localizedstring(forscriptcode:).md)
  Returns a localized string for a specified script code.
- [func localizedString(forVariantCode: String) -> String?](locale/localizedstring(forvariantcode:).md)
  Returns a localized string for a specified variant code.
### Getting the user’s preferred languages
- [static var preferredLanguages: [String]](locale/preferredlanguages.md)
  A list of the user’s preferred languages.
### Getting line and character direction for a language
- [static func characterDirection(forLanguage: String) -> Locale.LanguageDirection](locale/characterdirection(forlanguage:).md)
  Returns the character direction for a specified language code.
- [static func lineDirection(forLanguage: String) -> Locale.LanguageDirection](locale/linedirection(forlanguage:).md)
  Returns the line direction for a specified language code.
- [typealias LanguageDirection](locale/languagedirection.md)
  An alias for the standard set of language directions.
- [NSLocale.LanguageDirection](nslocale/languagedirection.md)
  The directions that a language may take across a page of text.
### Working with notification messages
- [Locale.CurrentLocaleDidChangeMessage](locale/currentlocaledidchangemessage.md)
### Using reference types
- [class NSLocale](nslocale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
### Structures
- [Locale.LanguageCode](locale/languagecode-swift.struct.md)
  An alphabetical code associated with a language.
- [Locale.Script](locale/script.md)
  The written script used with a given language.
### Type Properties
- [static var preferredLocales: [Locale]](locale/preferredlocales.md)
  Returns a list of the user’s preferred locales, as specified in Language & Region settings, taking into account any per-app language overrides.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale)*