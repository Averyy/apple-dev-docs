# decimalNumberWithMantissa:exponent:isNegative:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a decimal number equivalent to the number specified by the arguments.

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
+ (NSDecimalNumber *) decimalNumberWithMantissa:(unsigned long long) mantissa exponent:(short) exponent isNegative:(BOOL) flag;
```

#### Discussion

The arguments express a number in a kind of scientific notation that requires the mantissa to be an integer. So, for example, if the number to be represented is `–12.345`, it is expressed as `12345x10^–3`—`mantissa` is `12345`; `exponent` is `–3`; and `flag` is [`true`](../../Swift/true.md), as illustrated by the following example.

```objc
NSDecimalNumber *number = [NSDecimalNumber decimalNumberWithMantissa:12345
                                           exponent:-3
                                           isNegative:YES];
```

> ❗ **Important**:  `NSDecimalNumber` cannot represent negative zero. Initializing an `NSDecimalNumber` by passing 0 to `mantissa` and `exponent` and [`true`](../../Swift/true.md) to `flag` returns [`notANumber`](./notanumber.md) (`NaN`).

## Parameters

- `mantissa`: The mantissa for the new decimal number object.
- `exponent`: The exponent for the new decimal number object.
- `flag`: A Boolean value that specifies whether the sign of the number is negative.

## See Also

### Creating a Decimal Number
- [+ decimalNumberWithDecimal:](./decimalnumberwithdecimal_.md)
  Creates and returns a decimal number equivalent to a given decimal structure.
- [+ decimalNumberWithString:](./decimalnumberwithstring_.md)
  Creates a decimal number whose value is equivalent to that in a given numeric string.
- [+ decimalNumberWithString:locale:](./decimalnumberwithstring_locale_.md)
  Creates a decimal number whose value is equivalent to that in a given numeric string, interpreted using a given locale.
- [class var one: NSDecimalNumber](./one.md)
  A decimal number equivalent to the number 1.0.
- [class var zero: NSDecimalNumber](./zero.md)
  A decimal number equivalent to the number 0.0.
- [class var notANumber: NSDecimalNumber](./notanumber.md)
  A decimal number that specifies no number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/decimalnumberwithmantissa:exponent:isnegative:)*