# one

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A decimal number equivalent to the number 1.0.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
class var one: NSDecimalNumber { get }
```

```objc
@property (class, copy, readonly) NSDecimalNumber * one;
```

## Return Value

An `NSDecimalNumber` object equivalent to the number 1.0.

## See Also

### Creating a Decimal Number
- [class var zero: NSDecimalNumber](./zero.md)
  A decimal number equivalent to the number 0.0.
- [class var notANumber: NSDecimalNumber](./notanumber.md)
  A decimal number that specifies no number.
- [+ decimalNumberWithDecimal:](./decimalnumberwithdecimal_.md)
  Creates and returns a decimal number equivalent to a given decimal structure.
- [+ decimalNumberWithMantissa:exponent:isNegative:](./decimalnumberwithmantissa_exponent_isnegative_.md)
  Creates and returns a decimal number equivalent to the number specified by the arguments.
- [+ decimalNumberWithString:](./decimalnumberwithstring_.md)
  Creates a decimal number whose value is equivalent to that in a given numeric string.
- [+ decimalNumberWithString:locale:](./decimalnumberwithstring_locale_.md)
  Creates a decimal number whose value is equivalent to that in a given numeric string, interpreted using a given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/one)*