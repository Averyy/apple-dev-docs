# NSPositiveCurrencyFormatString

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A format string that specifies how positive numbers are printed when representing a currency value.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use the appropriate API from [`NumberFormatter`](./numberformatter.md) instead—see [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## Declaration

```c
extern NSString * const NSPositiveCurrencyFormatString;
```

#### Discussion

The default is `$9,999.00`.

## See Also

### Numeric Information
- [NSCurrencySymbol](./nscurrencysymbol.md)
  A string that specifies the symbol used to denote currency in this language.
- [NSDecimalDigits](./nsdecimaldigits.md)
  Strings that identify the decimal digits in addition to or instead of the ASCII digits.
- [NSDecimalSeparator](./nsdecimalseparator.md)
  A string that specifies the decimal separator.
- [NSInternationalCurrencyString](./nsinternationalcurrencystring.md)
  A string containing a three-letter abbreviation for currency, following the ISO 4217 standard.
- [NSNegativeCurrencyFormatString](./nsnegativecurrencyformatstring.md)
  A format string that specifies how negative numbers are printed when representing a currency value.
- [NSThousandsSeparator](./nsthousandsseparator.md)
  A string that specifies the separator character for the thousands place of a decimal number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositivecurrencyformatstring)*