# automatic

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A strategy to automatically configure sign display.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var automatic: CurrencyFormatStyleConfiguration.SignDisplayStrategy { get }
```

## See Also

### Specifying sign display strategy
- [static var never: CurrencyFormatStyleConfiguration.SignDisplayStrategy](./never.md)
  A strategy to never show the sign.
- [static var accounting: CurrencyFormatStyleConfiguration.SignDisplayStrategy](./accounting.md)
  A sign display strategy to use accounting principles.
- [static func accountingAlways(showZero: Bool) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy](./accountingalways%28showzero%29.md)
  A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.
- [static func always(showZero: Bool) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy](./always%28showzero%29.md)
  A sign display strategy to always show the sign, with a configurable behavior for handling zero values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/automatic)*