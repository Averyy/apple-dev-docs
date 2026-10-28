# availableLocaleIdentifiers

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The list of locale identifiers available on the system.

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
class var availableLocaleIdentifiers: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * availableLocaleIdentifiers;
```

## Discussion

A locale identifier starts with a language code, often includes a region code, and occasionally includes a script designator.  See [Locale IDs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15-SW9) for more information about the structure of a locale identifier.

Use [`localizedString(forLocaleIdentifier:)`](./localizedstring%28forlocaleidentifier%29.md) to obtain a human readable description of any of the locale identifiers in this list.

## See Also

### Related Documentation
- [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)
### Getting Known Identifiers and Codes
- [class var isoCountryCodes: [String]](./isocountrycodes.md)
  The list of known country or region codes.
- [class var isoLanguageCodes: [String]](./isolanguagecodes.md)
  The list of known language codes.
- [class var isoCurrencyCodes: [String]](./isocurrencycodes.md)
  The list of known currency codes.
- [class var commonISOCurrencyCodes: [String]](./commonisocurrencycodes.md)
  A list of commonly encountered currency codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/availablelocaleidentifiers)*