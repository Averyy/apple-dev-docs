# decimalNumberWithString:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a decimal number whose value is equivalent to that in a given numeric string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSDecimalNumber *) decimalNumberWithString:(NSString *) numberValue;
```

#### Discussion

Don’t use this method if `numberValue` has a fractional part, because the lack of a locale makes handling the decimal separator ambiguous. The separator is a period in some locales (like in the United States) and a comma in others (such as France).

To parse a numeric string with a fractional part, use [`decimalNumberWithString:locale:`](./decimalnumberwithstring_locale_.md) instead. When working with numeric representations with a known format, pass a fixed locale to ensure consistent results independent of the user’s current device settings. For localized parsing that uses the user’s current device settings, pass [`current`](../nslocale/current.md).

## Parameters

- `numberValue`: A numeric string.

  Besides digits, `numberValue` can include an initial `+` or `–`; a single `E` or `e`, to indicate the exponent of a number in scientific notation; and a single decimal separator character to divide the fractional from the integral part of the number. For a listing of acceptable and unacceptable strings, see [`decimalNumberWithString:locale:`](./decimalnumberwithstring_locale_.md).

## See Also

### Creating a Decimal Number
- [+ decimalNumberWithDecimal:](./decimalnumberwithdecimal_.md)
  Creates and returns a decimal number equivalent to a given decimal structure.
- [+ decimalNumberWithMantissa:exponent:isNegative:](./decimalnumberwithmantissa_exponent_isnegative_.md)
  Creates and returns a decimal number equivalent to the number specified by the arguments.
- [+ decimalNumberWithString:locale:](./decimalnumberwithstring_locale_.md)
  Creates a decimal number whose value is equivalent to that in a given numeric string, interpreted using a given locale.
- [class var one: NSDecimalNumber](./one.md)
  A decimal number equivalent to the number 1.0.
- [class var zero: NSDecimalNumber](./zero.md)
  A decimal number equivalent to the number 0.0.
- [class var notANumber: NSDecimalNumber](./notanumber.md)
  A decimal number that specifies no number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/decimalnumberwithstring:)*