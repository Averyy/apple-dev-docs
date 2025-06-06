# NSLocale

**Framework**: Foundation  
**Kind**: class

Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSLocale
```

#### Overview

In Swift, this object bridges to [`Locale`](locale.md); use [`NSLocale`](nslocale.md) when you need reference semantics or other Foundation-specific behavior.

You typically use a locale to format and interpret information about and according to the user’s customs and preferences.

You can initialize any number of locale instances with [`init(localeIdentifier:)`](nslocale/init(localeidentifier:).md) using one of the locale identifiers found in the [`availableLocaleIdentifiers`](nslocale/availablelocaleidentifiers.md) array. However, you usually use a locale configured to match the preferences of the current user.

Use the [`current`](nslocale/current.md) property to get the locale matching the current user’s preferences. If you need to be alerted when the user does make changes to region settings, register for the [`currentLocaleDidChangeNotification`](nslocale/currentlocaledidchangenotification.md) notification. Alternatively, you can use the [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md) property to get a locale that automatically updates with the user’s configuration settings:

You can inspect a locale by reading its properties, as listed in Getting Information About a Locale. For properties containing a code or identifier, you can then obtain a string suitable for presentation to the user with the methods listed in Getting Display Information About a Locale. For example, you can report the user’s language as a string localized in that language using the autoupdating locale obtained in the previous example:

You frequently use a locale in conjunction with a formatter. For example, the [`DateFormatter`](dateformatter.md) class has a [`locale`](dateformatter/locale.md) property that ensures dates are converted to strings that match the user’s expectations about date formatting. By default, this property indicates the user’s current locale, which is usually the behavior you want, but you can instead set it to another locale instance to obtain a different output. See [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for more information about working with formatters.

[`NSLocale`](nslocale.md) is  with its Core Foundation counterpart, [`CFLocale`](https://developer.apple.com/documentation/CoreFoundation/CFLocale). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Locale`](locale.md) structure, which bridges to the [`NSLocale`](nslocale.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`Locale`](locale.md) structure, which bridges to the [`NSLocale`](nslocale.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Initializing a Locale
- [init(localeIdentifier: String)](nslocale/init(localeidentifier:).md)
  Initializes a locale using a given locale identifier.
- [init?(coder: NSCoder)](nslocale/init(coder:).md)
  Returns a locale initialized from data in the given unarchiver.
### Getting the User’s Locale
- [class var autoupdatingCurrent: Locale](nslocale/autoupdatingcurrent.md)
  A locale which tracks the user’s current preferences.
- [class var current: Locale](nslocale/current.md)
  A locale representing the user’s region settings at the time the property is read.
- [class let currentLocaleDidChangeNotification: NSNotification.Name](nslocale/currentlocaledidchangenotification.md)
  A notification that indicates that the user’s locale changed.
- [class var system: Locale](nslocale/system.md)
  A locale representing the generic root values with little localization.
### Getting Known Identifiers and Codes
- [class var availableLocaleIdentifiers: [String]](nslocale/availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
- [class var isoCountryCodes: [String]](nslocale/isocountrycodes.md)
  The list of known country or region codes.
- [class var isoLanguageCodes: [String]](nslocale/isolanguagecodes.md)
  The list of known language codes.
- [class var isoCurrencyCodes: [String]](nslocale/isocurrencycodes.md)
  The list of known currency codes.
- [class var commonISOCurrencyCodes: [String]](nslocale/commonisocurrencycodes.md)
  A list of commonly encountered currency codes.
### Converting Between Identifiers
- [class func canonicalLocaleIdentifier(from: String) -> String](nslocale/canonicallocaleidentifier(from:).md)
  Returns the canonical identifier for a given locale identification string.
- [class func components(fromLocaleIdentifier: String) -> [String : String]](nslocale/components(fromlocaleidentifier:).md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](nslocale/localeidentifier(fromcomponents:).md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func canonicalLanguageIdentifier(from: String) -> String](nslocale/canonicallanguageidentifier(from:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](nslocale/localeidentifier(fromwindowslocalecode:).md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](nslocale/windowslocalecode(fromlocaleidentifier:).md)
  Returns a Window locale code from the locale identifier.
### Getting Information About a Locale
- [var localeIdentifier: String](nslocale/localeidentifier.md)
  The identifier for the locale.
- [var countryCode: String?](nslocale/countrycode.md)
  The country or region code for the locale.
- [var languageCode: String](nslocale/languagecode.md)
  The language code for the locale.
- [var scriptCode: String?](nslocale/scriptcode.md)
  The script code for the locale.
- [var variantCode: String?](nslocale/variantcode.md)
  The variant code for the locale.
- [var exemplarCharacterSet: CharacterSet](nslocale/exemplarcharacterset.md)
  The exemplar character set for the locale.
- [var collationIdentifier: String?](nslocale/collationidentifier.md)
  The collation identifier for the locale.
- [var collatorIdentifier: String](nslocale/collatoridentifier.md)
  The collator identifier for the locale.
- [var usesMetricSystem: Bool](nslocale/usesmetricsystem.md)
  A Boolean value that indicates whether the locale uses the metric system.
- [var decimalSeparator: String](nslocale/decimalseparator.md)
  The decimal separator for the locale.
- [var groupingSeparator: String](nslocale/groupingseparator.md)
  The grouping separator for the locale.
- [var currencyCode: String?](nslocale/currencycode.md)
  The currency code for the locale.
- [var currencySymbol: String](nslocale/currencysymbol.md)
  The currency symbol for the locale.
- [var calendarIdentifier: String](nslocale/calendaridentifier.md)
  The calendar identifier for the locale.
- [var quotationBeginDelimiter: String](nslocale/quotationbegindelimiter.md)
  The begin quotation symbol for the locale.
- [var quotationEndDelimiter: String](nslocale/quotationenddelimiter.md)
  The end quotation symbol for the locale.
- [var alternateQuotationBeginDelimiter: String](nslocale/alternatequotationbegindelimiter.md)
  The alternate begin quotation symbol for the locale.
- [var alternateQuotationEndDelimiter: String](nslocale/alternatequotationenddelimiter.md)
  The alternate end quotation symbol for the locale.
### Getting Display Information About a Locale
- [func localizedString(forLocaleIdentifier: String) -> String](nslocale/localizedstring(forlocaleidentifier:).md)
  Returns the localized string for the specified locale identifier.
- [func localizedString(forCountryCode: String) -> String?](nslocale/localizedstring(forcountrycode:).md)
  Returns the localized string for a country or region code.
- [func localizedString(forLanguageCode: String) -> String?](nslocale/localizedstring(forlanguagecode:).md)
  Returns the localized string for the specified language code.
- [func localizedString(forScriptCode: String) -> String?](nslocale/localizedstring(forscriptcode:).md)
  Returns the localized string for the specified script code.
- [func localizedString(forVariantCode: String) -> String?](nslocale/localizedstring(forvariantcode:).md)
  Returns the localized string for the specified variant code.
- [func localizedString(forCollationIdentifier: String) -> String?](nslocale/localizedstring(forcollationidentifier:).md)
  Returns the localized string for the specified collation identifier.
- [func localizedString(forCollatorIdentifier: String) -> String?](nslocale/localizedstring(forcollatoridentifier:).md)
  Returns the localized string for the specified collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](nslocale/localizedstring(forcurrencycode:).md)
  Returns the localized string for the specified currency code.
- [func localizedString(forCalendarIdentifier: String) -> String?](nslocale/localizedstring(forcalendaridentifier:).md)
  Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](locale-calendar-identifiers.md)
  The types of calendars.
### Accessing Locale Information by Key
- [func object(forKey: NSLocale.Key) -> Any?](nslocale/object(forkey:).md)
  Returns the value of the component corresponding to the specified key.
- [func displayName(forKey: NSLocale.Key, value: Any) -> String?](nslocale/displayname(forkey:value:).md)
  Returns the display name for the given locale component value.
- [NSLocale.Key](nslocale/key.md)
  The keys used to access components of a locale.
### Getting the User’s Preferred Languages
- [class var preferredLanguages: [String]](nslocale/preferredlanguages.md)
  An ordered list of the user’s preferred languages.
### Getting Line and Character Direction for a Language
- [class func characterDirection(forLanguage: String) -> NSLocale.LanguageDirection](nslocale/characterdirection(forlanguage:).md)
  Returns the direction of the sequence of characters in a line for the specified ISO language code.
- [class func lineDirection(forLanguage: String) -> NSLocale.LanguageDirection](nslocale/linedirection(forlanguage:).md)
  Returns the direction of the sequence of lines for the specified ISO language code.
- [NSLocale.LanguageDirection](nslocale/languagedirection.md)
  The directions that a language may take across a page of text.
### Instance Properties
- [var languageIdentifier: String](nslocale/languageidentifier.md)
- [var regionCode: String?](nslocale/regioncode.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Internationalization and Localization Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)
- [Data Formatting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale)*