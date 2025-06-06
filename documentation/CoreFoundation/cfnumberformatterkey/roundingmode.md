# roundingMode

**Framework**: Core Foundation  
**Kind**: property

Specifies how the last digit is rounded, as when `3.1415926535…` is rounded to three decimal places, as in `3.142`. See [`CFNumberFormatterRoundingMode`](cfnumberformatterroundingmode.md) for possible values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let roundingMode: CFNumberFormatterKey!
```

## See Also

- [static let currencyCode: CFNumberFormatterKey!](cfnumberformatterkey/currencycode.md)
  Specifies the currency code, a `CFString` object.
- [static let decimalSeparator: CFNumberFormatterKey!](cfnumberformatterkey/decimalseparator.md)
  Specifies the decimal separator, a `CFString` object.
- [static let currencyDecimalSeparator: CFNumberFormatterKey!](cfnumberformatterkey/currencydecimalseparator.md)
  Specifies the currency decimal separator, a `CFString` object.
- [static let alwaysShowDecimalSeparator: CFNumberFormatterKey!](cfnumberformatterkey/alwaysshowdecimalseparator.md)
  Specifies if the result of converting a value to a string should always contain the decimal separator, even if the number is an integer.
- [static let groupingSeparator: CFNumberFormatterKey!](cfnumberformatterkey/groupingseparator.md)
  Specifies the grouping separator, a `CFString` object.
- [static let useGroupingSeparator: CFNumberFormatterKey!](cfnumberformatterkey/usegroupingseparator.md)
  Specifies if the grouping separator should be used, a `CFBoolean` object.
- [static let percentSymbol: CFNumberFormatterKey!](cfnumberformatterkey/percentsymbol.md)
  Specifies the string that is used to represent the percent symbol, a `CFString` object.
- [static let zeroSymbol: CFNumberFormatterKey!](cfnumberformatterkey/zerosymbol.md)
  Specifies the string that is used to represent zero, a `CFString` object.
- [static let naNSymbol: CFNumberFormatterKey!](cfnumberformatterkey/nansymbol.md)
  Specifies the string that is used to represent NaN (“not a number”) when values are converted to strings, a `CFString` object.
- [static let infinitySymbol: CFNumberFormatterKey!](cfnumberformatterkey/infinitysymbol.md)
  Specifies the string that is used to represent the symbol for infinity, a `CFString` object.
- [static let minusSign: CFNumberFormatterKey!](cfnumberformatterkey/minussign.md)
  Specifies the symbol for the minus sign, a `CFString` object.
- [static let plusSign: CFNumberFormatterKey!](cfnumberformatterkey/plussign.md)
  Specifies the symbol for the plus sign, a `CFString` object.
- [static let currencySymbol: CFNumberFormatterKey!](cfnumberformatterkey/currencysymbol.md)
  Specifies the symbol for the currency, a `CFString` object.
- [static let exponentSymbol: CFNumberFormatterKey!](cfnumberformatterkey/exponentsymbol.md)
  Specifies the exponent symbol (“E” or “e”) in the scientific notation of numbers (for example, as in `1.0e+56`), a `CFString` object.
- [static let minIntegerDigits: CFNumberFormatterKey!](cfnumberformatterkey/minintegerdigits.md)
  Specifies the minimum number of integer digits before a decimal point, a `CFNumber` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey/roundingmode)*