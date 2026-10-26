# NSCurrencySymbol

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A string that specifies the symbol used to denote currency in this language.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: These constants are deprecated in OS X v10.5. Where there are replacements, you can typically find them in [`NumberFormatter`](./numberformatter.md) or [`NSLocale`](./nslocale.md)—for example, [`currencySymbol`](./numberformatter/currencysymbol.md), [`currencyDecimalSeparator`](./numberformatter/currencydecimalseparator.md), and [`thousandSeparator`](./numberformatter/thousandseparator.md)—otherwise you should use the patterns described in [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## Declaration

```c
extern NSString * const NSCurrencySymbol;
```

#### Discussion

The default is “$”.

## See Also

### Numeric Information
- [NSDecimalDigits](./nsdecimaldigits.md)
  Strings that identify the decimal digits in addition to or instead of the ASCII digits.
- [NSDecimalSeparator](./nsdecimalseparator.md)
  A string that specifies the decimal separator.
- [NSInternationalCurrencyString](./nsinternationalcurrencystring.md)
  A string containing a three-letter abbreviation for currency, following the ISO 4217 standard.
- [NSNegativeCurrencyFormatString](./nsnegativecurrencyformatstring.md)
  A format string that specifies how negative numbers are printed when representing a currency value.
- [NSPositiveCurrencyFormatString](./nspositivecurrencyformatstring.md)
  A format string that specifies how positive numbers are printed when representing a currency value.
- [NSThousandsSeparator](./nsthousandsseparator.md)
  A string that specifies the separator character for the thousands place of a decimal number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscurrencysymbol)*