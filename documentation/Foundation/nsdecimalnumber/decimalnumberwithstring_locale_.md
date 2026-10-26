# decimalNumberWithString:locale:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a decimal number whose value is equivalent to that in a given numeric string, interpreted using a given locale.

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
+ (NSDecimalNumber *) decimalNumberWithString:(NSString *) numberValue locale:(id) locale;
```

#### Discussion

The `locale` parameter determines whether the [`decimalSeparator`](../nslocale/key/decimalseparator.md) is a period (like in the United States) or a comma (like in France).

The following strings show examples of acceptable values for `numberValue`:

- `2500.6` (or `2500,6`, depending on locale)
- `–2500.6` (or `–2500,6`)
- `–2.5006e3` (or `–2,5006e3`)
- `–2.5006E3` (or `–2,5006E3`)

The following strings are unacceptable:

- `2,500.6`
- `2500 3/5`
- `2.5006x10e3`
- `two thousand five hundred and six tenths`

## Parameters

- `numberValue`: A numeric string.

  Besides digits, `numberValue` can include an initial `+` or `–`; a single `E` or `e`, to indicate the exponent of a number in scientific notation; and a single decimal separator character to divide the fractional from the integral part of the number.
- `locale`: A dictionary that defines the locale (specifically the [`decimalSeparator`](../nslocale/key/decimalseparator.md)) to use to interpret the number in `numberValue`.

## See Also

### Creating a Decimal Number
- [+ decimalNumberWithDecimal:](./decimalnumberwithdecimal_.md)
  Creates and returns a decimal number equivalent to a given decimal structure.
- [+ decimalNumberWithMantissa:exponent:isNegative:](./decimalnumberwithmantissa_exponent_isnegative_.md)
  Creates and returns a decimal number equivalent to the number specified by the arguments.
- [+ decimalNumberWithString:](./decimalnumberwithstring_.md)
  Creates a decimal number whose value is equivalent to that in a given numeric string.
- [class var one: NSDecimalNumber](./one.md)
  A decimal number equivalent to the number 1.0.
- [class var zero: NSDecimalNumber](./zero.md)
  A decimal number equivalent to the number 0.0.
- [class var notANumber: NSDecimalNumber](./notanumber.md)
  A decimal number that specifies no number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/decimalnumberwithstring:locale:)*