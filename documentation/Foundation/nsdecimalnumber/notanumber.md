# notANumber

**Framework**: Foundation  
**Kind**: property

A decimal number that specifies no number.

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
class var notANumber: NSDecimalNumber { get }
```

#### Return Value

An `NSDecimalNumber` object that specifies no number.

#### Discussion

Any arithmetic method receiving [`notANumber`](nsdecimalnumber/notanumber.md) as an argument returns [`notANumber`](nsdecimalnumber/notanumber.md).

This value can be a useful way of handling non-numeric data in an input file. This method can also be a useful response to calculation errors. For more information on calculation errors, see the [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md) method description in the [`NSDecimalNumberBehaviors`](nsdecimalnumberbehaviors.md) protocol specification.

## See Also

- [class var one: NSDecimalNumber](nsdecimalnumber/one.md)
  A decimal number equivalent to the number 1.0.
- [class var zero: NSDecimalNumber](nsdecimalnumber/zero.md)
  A decimal number equivalent to the number 0.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/notanumber)*