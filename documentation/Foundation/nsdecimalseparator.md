# NSDecimalSeparator

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A string that specifies the decimal separator.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`decimalSeparator`](./numberformatter/decimalseparator.md) or [`currencyDecimalSeparator`](./numberformatter/currencydecimalseparator.md) (`NSNumberFormatter`)  or retrieve the `NSLocaleDecimalSeparator` from the current locale instead.

## Declaration

```c
extern NSString * const NSDecimalSeparator;
```

#### Discussion

The decimal separator separates the ones place from the tenths place. The default is “`.`”.

## See Also

### Numeric Information
- [NSCurrencySymbol](./nscurrencysymbol.md)
  A string that specifies the symbol used to denote currency in this language.
- [NSDecimalDigits](./nsdecimaldigits.md)
  Strings that identify the decimal digits in addition to or instead of the ASCII digits.
- [NSInternationalCurrencyString](./nsinternationalcurrencystring.md)
  A string containing a three-letter abbreviation for currency, following the ISO 4217 standard.
- [NSNegativeCurrencyFormatString](./nsnegativecurrencyformatstring.md)
  A format string that specifies how negative numbers are printed when representing a currency value.
- [NSPositiveCurrencyFormatString](./nspositivecurrencyformatstring.md)
  A format string that specifies how positive numbers are printed when representing a currency value.
- [NSThousandsSeparator](./nsthousandsseparator.md)
  A string that specifies the separator character for the thousands place of a decimal number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalseparator)*