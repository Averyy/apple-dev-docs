# CFLocaleCreateCanonicalLanguageIdentifierFromString(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFLocaleCreateCanonicalLanguageIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFLocaleIdentifier!
```

```c
extern CFLocaleIdentifierCFLocaleCreateCanonicalLanguageIdentifierFromString(CFAllocatorRef allocator, CFStringRef localeIdentifier);
```

#### Return Value

A string that represents the canonical language identifier for the specified arbitrary locale identifier. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `localeIdentifier`: A string representation of an arbitrary locale identifier.

## See Also

### Getting and Creating Locale Identifiers
- [func CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(CFAllocator!, LangCode, RegionCode) -> CFLocaleIdentifier!](./cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes%28_,_,_%29.md)
  Returns a canonical locale identifier from given language and region codes.
- [func CFLocaleCreateCanonicalLocaleIdentifierFromString(CFAllocator!, CFString!) -> CFLocaleIdentifier!](./cflocalecreatecanonicallocaleidentifierfromstring%28_,_%29.md)
  Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [func CFLocaleCreateComponentsFromLocaleIdentifier(CFAllocator!, CFLocaleIdentifier!) -> CFDictionary!](./cflocalecreatecomponentsfromlocaleidentifier%28_,_%29.md)
  Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [func CFLocaleCreateLocaleIdentifierFromComponents(CFAllocator!, CFDictionary!) -> CFLocaleIdentifier!](./cflocalecreatelocaleidentifierfromcomponents%28_,_%29.md)
  Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(CFAllocator!, UInt32) -> CFLocaleIdentifier!](./cflocalecreatelocaleidentifierfromwindowslocalecode%28_,_%29.md)
  Returns a locale identifier from a Windows locale code.
- [func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier!) -> UInt32](./cflocalegetwindowslocalecodefromlocaleidentifier%28_%29.md)
  Returns a Windows locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreatecanonicallanguageidentifierfromstring(_:_:))*