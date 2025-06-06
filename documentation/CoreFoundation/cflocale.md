# CFLocale

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFLocale
```

#### Overview

Unicode operations such as collation and text boundary determination can be affected by the conventions of a particular language or region. CFLocale objects specify language-specific or region-specific information for locale-sensitive operations.

The CFLocale opaque type provides support for obtaining available locales, obtaining localized locale names, and converting among locale data formats. Locale identifiers in macOS follow the IETF’s [`BCP 47`](https://developer.apple.comhttp://www.rfc-editor.org/rfc/bcp/bcp47.txt). CFLocale never uses Script Manager codes (except for the legacy support provided by [`CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(_:_:_:)`](cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(_:_:_:).md))—the Script Manager and all its concepts are deprecated.

For more information on locale identifiers, read [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i). It is also useful to read the ICU’s [`User Guide for the Locale Class`](https://developer.apple.comhttp://icu-project.org/userguide/locale.html).

CFLocale is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSLocale`](https://developer.apple.com/documentation/Foundation/NSLocale). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSLocale *` parameter, you can pass in a `CFLocaleRef`, and in a function where you see a `CFLocaleRef` parameter, you can pass in an `NSLocale` instance. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Locale
- [func CFLocaleCopyCurrent() -> CFLocale!](cflocalecopycurrent().md)
  Returns a copy of the logical locale for the current user.
- [func CFLocaleCreate(CFAllocator!, CFLocaleIdentifier!) -> CFLocale!](cflocalecreate(_:_:).md)
  Creates a locale for the given arbitrary locale identifier.
- [func CFLocaleCreateCopy(CFAllocator!, CFLocale!) -> CFLocale!](cflocalecreatecopy(_:_:).md)
  Returns a copy of a locale.
- [func CFLocaleGetSystem() -> CFLocale!](cflocalegetsystem().md)
  Returns the root, canonical locale.
### Getting System Locale Information
- [func CFLocaleCopyAvailableLocaleIdentifiers() -> CFArray!](cflocalecopyavailablelocaleidentifiers().md)
  Returns an array of CFString objects that represents all locales for which locale data is available.
### Getting ISO Information
- [func CFLocaleCopyISOCountryCodes() -> CFArray!](cflocalecopyisocountrycodes().md)
  Returns an array of CFString objects that represents all known legal ISO country codes.
- [func CFLocaleCopyISOLanguageCodes() -> CFArray!](cflocalecopyisolanguagecodes().md)
  Returns an array of CFString objects that represents all known legal ISO language codes.
- [func CFLocaleCopyISOCurrencyCodes() -> CFArray!](cflocalecopyisocurrencycodes().md)
  Returns an array of CFString objects that represents all known legal ISO currency codes.
- [func CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!](cflocalecopycommonisocurrencycodes().md)
  Returns an array of strings that represents ISO currency codes for currencies in common use.
### Language Preferences
- [func CFLocaleCopyPreferredLanguages() -> CFArray!](cflocalecopypreferredlanguages().md)
  Returns the array of canonicalized language IDs that the user prefers.
### Getting Information About a Locale
- [func CFLocaleCopyDisplayNameForPropertyValue(CFLocale!, CFLocaleKey!, CFString!) -> CFString!](cflocalecopydisplaynameforpropertyvalue(_:_:_:).md)
  Returns the display name for the given value.
- [func CFLocaleGetValue(CFLocale!, CFLocaleKey!) -> CFTypeRef!](cflocalegetvalue(_:_:).md)
  Returns the corresponding value for the given key of a locale’s key-value pair.
- [func CFLocaleGetIdentifier(CFLocale!) -> CFLocaleIdentifier!](cflocalegetidentifier(_:).md)
  Returns the given locale’s identifier.
### Getting and Creating Locale Identifiers
- [func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(CFAllocator!, LangCode, RegionCode) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(_:_:_:).md)
  Returns a canonical locale identifier from given language and region codes.
- [func CFLocaleCreateCanonicalLanguageIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallanguageidentifierfromstring(_:_:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [func CFLocaleCreateCanonicalLocaleIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromstring(_:_:).md)
  Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [func CFLocaleCreateComponentsFromLocaleIdentifier(CFAllocator!, CFLocaleIdentifier!) -> CFDictionary!](cflocalecreatecomponentsfromlocaleidentifier(_:_:).md)
  Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [func CFLocaleCreateLocaleIdentifierFromComponents(CFAllocator!, CFDictionary!) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromcomponents(_:_:).md)
  Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromwindowslocalecode(_:_:).md)
  Returns a locale identifier from a Windows locale code.
- [func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier!) -> UInt32](cflocalegetwindowslocalecodefromlocaleidentifier(_:).md)
  Returns a Windows locale code from the locale identifier.
### Getting Line and Character Direction for a Language
- [func CFLocaleGetLanguageCharacterDirection(CFString!) -> CFLocaleLanguageDirection](cflocalegetlanguagecharacterdirection(_:).md)
  Returns the character direction for the specified ISO language code.
- [func CFLocaleGetLanguageLineDirection(CFString!) -> CFLocaleLanguageDirection](cflocalegetlanguagelinedirection(_:).md)
  Returns the line direction for the specified ISO language code.
### Getting the CFLocale Type ID
- [func CFLocaleGetTypeID() -> CFTypeID](cflocalegettypeid().md)
  Returns the type identifier for the CFLocale opaque type.
### Constants
- [enum CFLocaleLanguageDirection](cflocalelanguagedirection.md)
  These constants describe the text direction for a language. They are returned by the functions [`CFLocaleGetLanguageCharacterDirection(_:)`](cflocalegetlanguagecharacterdirection(_:).md) and [`CFLocaleGetLanguageLineDirection(_:)`](cflocalegetlanguagelinedirection(_:).md).
- [Locale Property Keys](locale-property-keys.md)
  Predefined locale keys used to get property values.
- [Locale Calendar Identifiers](locale-calendar-identifiers.md)
  Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](locale-change-notification.md)
  Identifier for notification sent if the current locale changes.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Internationalization and Localization Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocale)*