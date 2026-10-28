# CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Windows locale code from the locale identifier.

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
func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: CFLocaleIdentifier!) -> UInt32
```

```c
extern uint32_t CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier localeIdentifier);
```

## Return Value

The Windows locale code.

## Parameters

- `localeIdentifier`: The locale identifier.

## See Also

### Getting and Creating Locale Identifiers
- [func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(CFAllocator!, LangCode, RegionCode) -> CFLocaleIdentifier!](./cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes%28_,_,_%29.md)
  Returns a canonical locale identifier from given language and region codes.
- [func CFLocaleCreateCanonicalLanguageIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](./cflocalecreatecanonicallanguageidentifierfromstring%28_,_%29.md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [func CFLocaleCreateCanonicalLocaleIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](./cflocalecreatecanonicallocaleidentifierfromstring%28_,_%29.md)
  Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [func CFLocaleCreateComponentsFromLocaleIdentifier(CFAllocator!, CFLocaleIdentifier!) -> CFDictionary!](./cflocalecreatecomponentsfromlocaleidentifier%28_,_%29.md)
  Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [func CFLocaleCreateLocaleIdentifierFromComponents(CFAllocator!, CFDictionary!) -> CFLocaleIdentifier!](./cflocalecreatelocaleidentifierfromcomponents%28_,_%29.md)
  Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFLocaleIdentifier!](./cflocalecreatelocaleidentifierfromwindowslocalecode%28_,_%29.md)
  Returns a locale identifier from a Windows locale code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalegetwindowslocalecodefromlocaleidentifier(_:))*