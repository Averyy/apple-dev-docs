# CFNumberFormatterKey

**Framework**: Core Foundation  
**Kind**: struct

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
struct CFNumberFormatterKey
```

## Topics

### Type Properties
- [static let alwaysShowDecimalSeparator: CFNumberFormatterKey!](cfnumberformatterkey/alwaysshowdecimalseparator.md)
  Specifies if the result of converting a value to a string should always contain the decimal separator, even if the number is an integer.
- [static let currencyCode: CFNumberFormatterKey!](cfnumberformatterkey/currencycode.md)
  Specifies the currency code, a `CFString` object.
- [static let currencyDecimalSeparator: CFNumberFormatterKey!](cfnumberformatterkey/currencydecimalseparator.md)
  Specifies the currency decimal separator, a `CFString` object.
- [static let currencyGroupingSeparator: CFNumberFormatterKey!](cfnumberformatterkey/currencygroupingseparator.md)
  Specifies the grouping symbol to use when placing a currency value within a string, a `CFString` object.
- [static let currencySymbol: CFNumberFormatterKey!](cfnumberformatterkey/currencysymbol.md)
  Specifies the symbol for the currency, a `CFString` object.
- [static let decimalSeparator: CFNumberFormatterKey!](cfnumberformatterkey/decimalseparator.md)
  Specifies the decimal separator, a `CFString` object.
- [static let defaultFormat: CFNumberFormatterKey!](cfnumberformatterkey/defaultformat.md)
  The original format string for the formatter (given the date and time style and locale specified at creation), a `CFString` object.
- [static let exponentSymbol: CFNumberFormatterKey!](cfnumberformatterkey/exponentsymbol.md)
  Specifies the exponent symbol (“E” or “e”) in the scientific notation of numbers (for example, as in `1.0e+56`), a `CFString` object.
- [static let formatWidth: CFNumberFormatterKey!](cfnumberformatterkey/formatwidth.md)
  Specifies the width of a formatted number within a string that is either left justified or right justified based on the value of [`paddingPosition`](cfnumberformatterkey/paddingposition.md), a `CFNumber` object.
- [static let groupingSeparator: CFNumberFormatterKey!](cfnumberformatterkey/groupingseparator.md)
  Specifies the grouping separator, a `CFString` object.
- [static let groupingSize: CFNumberFormatterKey!](cfnumberformatterkey/groupingsize.md)
  Specifies how often the “thousands” or grouping separator appears, as in “10,000,000”, a `CFNumber` object.
- [static let infinitySymbol: CFNumberFormatterKey!](cfnumberformatterkey/infinitysymbol.md)
  Specifies the string that is used to represent the symbol for infinity, a `CFString` object.
- [static let internationalCurrencySymbol: CFNumberFormatterKey!](cfnumberformatterkey/internationalcurrencysymbol.md)
  Specifies the international currency symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let isLenient: CFNumberFormatterKey!](cfnumberformatterkey/islenient.md)
  Specifies whether the formatter is lenient, a`CFBoolean` object.
- [static let maxFractionDigits: CFNumberFormatterKey!](cfnumberformatterkey/maxfractiondigits.md)
  Specifies the maximum number of digits after a decimal point, a `CFNumber` object.
- [static let maxIntegerDigits: CFNumberFormatterKey!](cfnumberformatterkey/maxintegerdigits.md)
  Specifies the maximum number of integer digits before a decimal point, a `CFNumber` object.
- [static let maxSignificantDigits: CFNumberFormatterKey!](cfnumberformatterkey/maxsignificantdigits.md)
  Specifies the maximum number of significant digits to use, a`CFNumber` object.
- [static let minFractionDigits: CFNumberFormatterKey!](cfnumberformatterkey/minfractiondigits.md)
  Specifies the minimum number of digits after a decimal point, a `CFNumber` object.
- [static let minIntegerDigits: CFNumberFormatterKey!](cfnumberformatterkey/minintegerdigits.md)
  Specifies the minimum number of integer digits before a decimal point, a `CFNumber` object.
- [static let minSignificantDigits: CFNumberFormatterKey!](cfnumberformatterkey/minsignificantdigits.md)
  Specifies the minimum number of significant digits to use, a`CFNumber` object.
- [static let minusSign: CFNumberFormatterKey!](cfnumberformatterkey/minussign.md)
  Specifies the symbol for the minus sign, a `CFString` object.
- [static let multiplier: CFNumberFormatterKey!](cfnumberformatterkey/multiplier.md)
  Specifies the multiplier to use when placing a formatted number within a string, a `CFNumber` object.
- [static let naNSymbol: CFNumberFormatterKey!](cfnumberformatterkey/nansymbol.md)
  Specifies the string that is used to represent NaN (“not a number”) when values are converted to strings, a `CFString` object.
- [static let negativePrefix: CFNumberFormatterKey!](cfnumberformatterkey/negativeprefix.md)
  Specifies the minus sign prefix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let negativeSuffix: CFNumberFormatterKey!](cfnumberformatterkey/negativesuffix.md)
  Specifies the minus sign suffix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let paddingCharacter: CFNumberFormatterKey!](cfnumberformatterkey/paddingcharacter.md)
  Specifies the padding character to use when placing a formatted number within a string, a `CFString` object.
- [static let paddingPosition: CFNumberFormatterKey!](cfnumberformatterkey/paddingposition.md)
  Specifies the position of a formatted number within a string, a `CFNumber` object.
- [static let perMillSymbol: CFNumberFormatterKey!](cfnumberformatterkey/permillsymbol.md)
  Specifies the per mill (1/1000) symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let percentSymbol: CFNumberFormatterKey!](cfnumberformatterkey/percentsymbol.md)
  Specifies the string that is used to represent the percent symbol, a `CFString` object.
- [static let plusSign: CFNumberFormatterKey!](cfnumberformatterkey/plussign.md)
  Specifies the symbol for the plus sign, a `CFString` object.
- [static let positivePrefix: CFNumberFormatterKey!](cfnumberformatterkey/positiveprefix.md)
  Specifies the plus sign prefix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let positiveSuffix: CFNumberFormatterKey!](cfnumberformatterkey/positivesuffix.md)
  Specifies the plus sign suffix symbol to use when placing a formatted number within a string, a `CFString` object.
- [static let roundingIncrement: CFNumberFormatterKey!](cfnumberformatterkey/roundingincrement.md)
  Specifies a positive rounding increment, or `0.0` to disable rounding, a `CFNumber` object.
- [static let roundingMode: CFNumberFormatterKey!](cfnumberformatterkey/roundingmode.md)
  Specifies how the last digit is rounded, as when `3.1415926535…` is rounded to three decimal places, as in `3.142`. See [`CFNumberFormatterRoundingMode`](cfnumberformatterroundingmode.md) for possible values.
- [static let secondaryGroupingSize: CFNumberFormatterKey!](cfnumberformatterkey/secondarygroupingsize.md)
  Specifies how often the secondary grouping separator appears, a `CFNumber` object.
- [static let useGroupingSeparator: CFNumberFormatterKey!](cfnumberformatterkey/usegroupingseparator.md)
  Specifies if the grouping separator should be used, a `CFBoolean` object.
- [static let useSignificantDigits: CFNumberFormatterKey!](cfnumberformatterkey/usesignificantdigits.md)
  Specifies the whether the formatter uses significant digits, a `CFBoolean` object.
- [static let zeroSymbol: CFNumberFormatterKey!](cfnumberformatterkey/zerosymbol.md)
  Specifies the string that is used to represent zero, a `CFString` object.
- [static let minGroupingDigits: CFNumberFormatterKey!](cfnumberformatterkey/mingroupingdigits.md)
### Initializers
- [init(rawValue: CFString)](cfnumberformatterkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CFAllocatorTypeID](cfallocatortypeid.md)
- [struct CFCalendarIdentifier](cfcalendaridentifier.md)
- [struct CFDateFormatterKey](cfdateformatterkey.md)
- [typealias CFErrorDomain](cferrordomain.md)
- [struct CFLocaleIdentifier](cflocaleidentifier.md)
- [struct CFLocaleKey](cflocalekey.md)
- [struct CFNotificationName](cfnotificationname.md)
- [struct CFRunLoopMode](cfrunloopmode.md)
- [struct CFStreamPropertyKey](cfstreampropertykey.md)
- [typealias CFTypeRef](cftyperef.md)
  An untyped “generic” reference to any Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey)*