# CurrencyFormatStyleConfiguration.SignDisplayStrategy

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A structure used to configure sign display strategies for currency format styles.

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
struct SignDisplayStrategy
```

## Topics

### Specifying sign display strategy
- [static var never: CurrencyFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/never.md)
  A strategy to never show the sign.
- [static var automatic: CurrencyFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/automatic.md)
  A strategy to automatically configure sign display.
- [static var accounting: CurrencyFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/accounting.md)
  A sign display strategy to use accounting principles.
- [static func accountingAlways(showZero: Bool) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/accountingalways%28showzero%29.md)
  A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.
- [static func always(showZero: Bool) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/always%28showzero%29.md)
  A sign display strategy to always show the sign, with a configurable behavior for handling zero values.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying Configuration
- [CurrencyFormatStyleConfiguration.Grouping](./grouping.md)
  The type used to configure grouping for currency format styles.
- [CurrencyFormatStyleConfiguration.Precision](./precision.md)
  The type used to configure precision for currency format styles.
- [CurrencyFormatStyleConfiguration.DecimalSeparatorDisplayStrategy](./decimalseparatordisplaystrategy.md)
  The type used to configure decimal separator display strategies for currency format styles.
- [CurrencyFormatStyleConfiguration.RoundingRule](./roundingrule.md)
  The type used to configure rounding rules for currency format styles.
- [CurrencyFormatStyleConfiguration.Presentation](./presentation.md)
  A structure used to configure the presentation of currency format styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy)*