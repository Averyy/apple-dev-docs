# CFLocaleCreateComponentsFromLocaleIdentifier(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.

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
func CFLocaleCreateComponentsFromLocaleIdentifier(_ allocator: CFAllocator!, _ localeID: CFLocaleIdentifier!) -> CFDictionary!
```

#### Return Value

A dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs. Returns `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The dictionary keys are the constant CFString objects that correspond to the locale ID components; the values correspond to constants where available. For example: the string “en_US@calendar=japanese” yields a dictionary with three entries: `kCFLocaleLanguageCode``=en`, `kCFLocaleCountryCode``=US`, and `kCFLocaleCalendarIdentifier``=``kCFJapaneseCalendar`. See also [`CFLocaleCreateLocaleIdentifierFromComponents(_:_:)`](cflocalecreatelocaleidentifierfromcomponents(_:_:).md).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `localeID`: The locale ID to use when creating the locale dictionary.

## See Also

- [func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(CFAllocator!, LangCode, RegionCode) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(_:_:_:).md)
  Returns a canonical locale identifier from given language and region codes.
- [func CFLocaleCreateCanonicalLanguageIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallanguageidentifierfromstring(_:_:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [func CFLocaleCreateCanonicalLocaleIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromstring(_:_:).md)
  Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [func CFLocaleCreateLocaleIdentifierFromComponents(CFAllocator!, CFDictionary!) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromcomponents(_:_:).md)
  Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromwindowslocalecode(_:_:).md)
  Returns a locale identifier from a Windows locale code.
- [func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier!) -> UInt32](cflocalegetwindowslocalecodefromlocaleidentifier(_:).md)
  Returns a Windows locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreatecomponentsfromlocaleidentifier(_:_:))*