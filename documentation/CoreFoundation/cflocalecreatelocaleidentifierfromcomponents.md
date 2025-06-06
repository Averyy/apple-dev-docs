# CFLocaleCreateLocaleIdentifierFromComponents(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.

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
func CFLocaleCreateLocaleIdentifierFromComponents(_ allocator: CFAllocator!, _ dictionary: CFDictionary!) -> CFLocaleIdentifier!
```

#### Return Value

A locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from `dictionary`. Returns `NULL` if there was a problem creating the string. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Reverses the actions of [`CFLocaleCreateComponentsFromLocaleIdentifier(_:_:)`](cflocalecreatecomponentsfromlocaleidentifier(_:_:).md), creating a single string from the data in the specified dictionary. For example, the dictionary {`kCFLocaleLanguageCode``=en``,` `kCFLocaleCountryCode``=US``,` `kCFLocaleCalendarIdentifier``=``kCFJapaneseCalendar``}` becomes `"en_US@calendar=japanese"`.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `dictionary`: The dictionary to use when creating the locale identifier.

## See Also

- [func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(CFAllocator!, LangCode, RegionCode) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(_:_:_:).md)
  Returns a canonical locale identifier from given language and region codes.
- [func CFLocaleCreateCanonicalLanguageIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallanguageidentifierfromstring(_:_:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [func CFLocaleCreateCanonicalLocaleIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromstring(_:_:).md)
  Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [func CFLocaleCreateComponentsFromLocaleIdentifier(CFAllocator!, CFLocaleIdentifier!) -> CFDictionary!](cflocalecreatecomponentsfromlocaleidentifier(_:_:).md)
  Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromwindowslocalecode(_:_:).md)
  Returns a locale identifier from a Windows locale code.
- [func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier!) -> UInt32](cflocalegetwindowslocalecodefromlocaleidentifier(_:).md)
  Returns a Windows locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreatelocaleidentifierfromcomponents(_:_:))*