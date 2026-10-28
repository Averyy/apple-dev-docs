# decimalNumberWithDecimal:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a decimal number equivalent to a given decimal structure.

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
+ (NSDecimalNumber *) decimalNumberWithDecimal:(NSDecimal) dcm;
```

## Return Value

An `NSDecimalNumber` object  equivalent to `dcm`.

## Discussion

You can initialize `dcm` programmatically or generate it using the `NSScanner` method, [`scanDecimal(_:)`](../scanner/scandecimal%28_%29.md)

## Parameters

- `dcm`: An `NSDecimal` structure that specifies the value for the new decimal number object.

## See Also

### Related Documentation
- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)
### Creating a Decimal Number
- [+ decimalNumberWithMantissa:exponent:isNegative:](./decimalnumberwithmantissa_exponent_isnegative_.md)
  Creates and returns a decimal number equivalent to the number specified by the arguments.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/decimalnumberwithdecimal:)*