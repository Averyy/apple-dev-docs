# Number Formatter Property Keys

**Framework**: Core Foundation

The keys used in key-value pairs to specify the value of number formatter properties.

#### Overview

The values for these keys are all `CFType` objects. The specific types for each key are specified above.

## Topics

### Constants
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
- [static let maxIntegerDigits: CFNumberFormatterKey!](cfnumberformatterkey/maxintegerdigits.md)
  Specifies the maximum number of integer digits before a decimal point, a `CFNumber` object.
- [static let minFractionDigits: CFNumberFormatterKey!](cfnumberformatterkey/minfractiondigits.md)
  Specifies the minimum number of digits after a decimal point, a `CFNumber` object.
- [static let maxFractionDigits: CFNumberFormatterKey!](cfnumberformatterkey/maxfractiondigits.md)
  Specifies the maximum number of digits after a decimal point, a `CFNumber` object.
- [static let groupingSize: CFNumberFormatterKey!](cfnumberformatterkey/groupingsize.md)
  Specifies how often the “thousands” or grouping separator appears, as in “10,000,000”, a `CFNumber` object.
- [static let secondaryGroupingSize: CFNumberFormatterKey!](cfnumberformatterkey/secondarygroupingsize.md)
  Specifies how often the secondary grouping separator appears, a `CFNumber` object.
- [static let roundingMode: CFNumberFormatterKey!](cfnumberformatterkey/roundingmode.md)
  Specifies how the last digit is rounded, as when `3.1415926535…` is rounded to three decimal places, as in `3.142`. See [`CFNumberFormatterRoundingMode`](cfnumberformatterroundingmode.md) for possible values.
- [static let roundingIncrement: CFNumberFormatterKey!](cfnumberformatterkey/roundingincrement.md)
  Specifies a positive rounding increment, or `0.0` to disable rounding, a `CFNumber` object.
- [static let formatWidth: CFNumberFormatterKey!](cfnumberformatterkey/formatwidth.md)
  Specifies the width of a formatted number within a string that is either left justified or right justified based on the value of [`paddingPosition`](cfnumberformatterkey/paddingposition.md), a `CFNumber` object.
- [static let paddingPosition: CFNumberFormatterKey!](cfnumberformatterkey/paddingposition.md)
  Specifies the position of a formatted number within a string, a `CFNumber` object.
- [static let paddingCharacter: CFNumberFormatterKey!](cfnumberformatterkey/paddingcharacter.md)
  Specifies the padding character to use when placing a formatted number within a string, a `CFString` object.
- [static let defaultFormat: CFNumberFormatterKey!](cfnumberformatterkey/defaultformat.md)
  The original format string for the formatter (given the date and time style and locale specified at creation), a `CFString` object.
- [static let multiplier: CFNumberFormatterKey!](cfnumberformatterkey/multiplier.md)
  Specifies the multiplier to use when placing a formatted number within a string, a `CFNumber` object.
- [static let positivePrefix: CFNumberFormatterKey!](cfnumberformatterkey/positiveprefix.md)
  Specifies the plus sign prefix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let positiveSuffix: CFNumberFormatterKey!](cfnumberformatterkey/positivesuffix.md)
  Specifies the plus sign suffix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let negativePrefix: CFNumberFormatterKey!](cfnumberformatterkey/negativeprefix.md)
  Specifies the minus sign prefix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let negativeSuffix: CFNumberFormatterKey!](cfnumberformatterkey/negativesuffix.md)
  Specifies the minus sign suffix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let perMillSymbol: CFNumberFormatterKey!](cfnumberformatterkey/permillsymbol.md)
  Specifies the per mill (1/1000) symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let internationalCurrencySymbol: CFNumberFormatterKey!](cfnumberformatterkey/internationalcurrencysymbol.md)
  Specifies the international currency symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let currencyGroupingSeparator: CFNumberFormatterKey!](cfnumberformatterkey/currencygroupingseparator.md)
  Specifies the grouping symbol to use when placing a currency value within a string, a `CFString` object.
- [static let isLenient: CFNumberFormatterKey!](cfnumberformatterkey/islenient.md)
  Specifies whether the formatter is lenient, a`CFBoolean` object.
- [static let useSignificantDigits: CFNumberFormatterKey!](cfnumberformatterkey/usesignificantdigits.md)
  Specifies the whether the formatter uses significant digits, a `CFBoolean` object.
- [static let minSignificantDigits: CFNumberFormatterKey!](cfnumberformatterkey/minsignificantdigits.md)
  Specifies the minimum number of significant digits to use, a`CFNumber` object.
- [static let maxSignificantDigits: CFNumberFormatterKey!](cfnumberformatterkey/maxsignificantdigits.md)
  Specifies the maximum number of significant digits to use, a`CFNumber` object.

## See Also

- [Number Formatter Styles](number-formatter-styles.md)
  Predefined number format styles.
- [Number Format Options](number_format_options.md)
  These constants are used to specify how numbers should be parsed.
- [enum CFNumberFormatterRoundingMode](cfnumberformatterroundingmode.md)
  These constants are used to specify how numbers should be rounded.
- [Padding Positions](padding-positions.md)
  These constants are used to specify how numbers should be padded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/number-formatter-property-keys)*