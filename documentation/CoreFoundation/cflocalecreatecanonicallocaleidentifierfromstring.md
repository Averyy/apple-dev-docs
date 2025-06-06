# CFLocaleCreateCanonicalLocaleIdentifierFromString(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.

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
func CFLocaleCreateCanonicalLocaleIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFLocaleIdentifier!
```

#### Return Value

A canonical locale identifier created by mapping the arbitrary locale identification string to the canonical identifier for the corresponding locale (for example, “en”). Returns `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `localeIdentifier`: A string representation of an arbitrary locale identifier (for example, “English”).

## See Also

- [func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(CFAllocator!, LangCode, RegionCode) -> CFLocaleIdentifier!](cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(_:_:_:).md)
  Returns a canonical locale identifier from given language and region codes.
- [func CFLocaleCreateCanonicalLanguageIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](cflocalecreatecanonicallanguageidentifierfromstring(_:_:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [func CFLocaleCreateComponentsFromLocaleIdentifier(CFAllocator!, CFLocaleIdentifier!) -> CFDictionary!](cflocalecreatecomponentsfromlocaleidentifier(_:_:).md)
  Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [func CFLocaleCreateLocaleIdentifierFromComponents(CFAllocator!, CFDictionary!) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromcomponents(_:_:).md)
  Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFLocaleIdentifier!](cflocalecreatelocaleidentifierfromwindowslocalecode(_:_:).md)
  Returns a locale identifier from a Windows locale code.
- [func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier!) -> UInt32](cflocalegetwindowslocalecodefromlocaleidentifier(_:).md)
  Returns a Windows locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreatecanonicallocaleidentifierfromstring(_:_:))*