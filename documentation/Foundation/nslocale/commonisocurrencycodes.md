# commonISOCurrencyCodes

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A list of commonly encountered currency codes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var commonISOCurrencyCodes: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * commonISOCurrencyCodes;
```

## Discussion

Common codes may include, for example, `"AED"`, `"AUD"`, `"BZD"`, `"DKK"`, `"EUR"`, `"GBP"`, `"JPY"`, `"KES"`, `"MXN"`, `"OMR"`, `"STD"`, `"USD"`, `"XCD"`, and `"ZWD"`.

## See Also

### Getting Known Identifiers and Codes
- [class var availableLocaleIdentifiers: [String]](./availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
- [class var isoCountryCodes: [String]](./isocountrycodes.md)
  The list of known country or region codes.
- [class var isoLanguageCodes: [String]](./isolanguagecodes.md)
  The list of known language codes.
- [class var isoCurrencyCodes: [String]](./isocurrencycodes.md)
  The list of known currency codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/commonisocurrencycodes)*