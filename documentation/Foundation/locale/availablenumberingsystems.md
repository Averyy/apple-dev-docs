# availableNumberingSystems

**Framework**: Foundation  
**Kind**: property

An array containing all the valid numbering systems for the locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var availableNumberingSystems: [Locale.NumberingSystem] { get }
```

#### Discussion

The following snippet creates a locale for Arabic as used in United Arab Emirites. For this locale, there are two numbering systems available: `latn` (Latin digits) and `arab` (Arabic-Indic digits).

```swift
let uae = Locale(identifier: "ar-AE") // Arabic / U.A.E.
let numberingSystems = uae.availableNumberingSystems
print("\(numberingSystems.map{$0.identifier})") // ["latn","arab"]
```

## See Also

- [var currency: Locale.Currency?](locale/currency-swift.property.md)
  The currency used by the locale.
- [Locale.Currency](locale/currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem](locale/measurementsystem-swift.property.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](locale/measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](locale/numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [Locale.NumberingSystem](locale/numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/availablenumberingsystems)*