# CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a locale identifier from a Windows locale code.

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
func CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(_ allocator: CFAllocator!, _ lcid: UInt32) -> CFLocaleIdentifier!
```

#### Return Value

The locale identifier.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `lcid`: The Windows locale code.

## See Also

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
- [func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(CFLocaleIdentifier!) -> UInt32](cflocalegetwindowslocalecodefromlocaleidentifier(_:).md)
  Returns a Windows locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreatelocaleidentifierfromwindowslocalecode(_:_:))*