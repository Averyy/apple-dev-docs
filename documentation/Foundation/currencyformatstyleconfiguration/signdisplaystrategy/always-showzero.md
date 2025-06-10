# always(showZero:)

**Framework**: Foundation  
**Kind**: method

A sign display strategy to always show the sign, with a configurable behavior for handling zero values.

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
static func always(showZero: Bool = true) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy
```

#### Return Value

A sign display strategy that always displays the sign, and uses the specified handling of zero values.

## Parameters

- `showZero`: A Boolean value that indicates whether to show the sign symbol on zero values. Defaults to  .

## See Also

- [static var never: CurrencyFormatStyleConfiguration.SignDisplayStrategy](currencyformatstyleconfiguration/signdisplaystrategy/never.md)
  A strategy to never show the sign.
- [static var automatic: CurrencyFormatStyleConfiguration.SignDisplayStrategy](currencyformatstyleconfiguration/signdisplaystrategy/automatic.md)
  A strategy to automatically configure sign display.
- [static var accounting: CurrencyFormatStyleConfiguration.SignDisplayStrategy](currencyformatstyleconfiguration/signdisplaystrategy/accounting.md)
  A sign display strategy to use accounting principles.
- [static func accountingAlways(showZero: Bool) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy](currencyformatstyleconfiguration/signdisplaystrategy/accountingalways(showzero:).md)
  A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/always(showzero:))*