# isoCountryCodes

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The list of known country or region codes.

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
class var isoCountryCodes: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * ISOCountryCodes;
```

## Discussion

Not all country or region codes have supporting locale data in the system.

## See Also

### Getting Known Identifiers and Codes
- [class var availableLocaleIdentifiers: [String]](./availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
- [class var isoLanguageCodes: [String]](./isolanguagecodes.md)
  The list of known language codes.
- [class var isoCurrencyCodes: [String]](./isocurrencycodes.md)
  The list of known currency codes.
- [class var commonISOCurrencyCodes: [String]](./commonisocurrencycodes.md)
  A list of commonly encountered currency codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/isocountrycodes)*