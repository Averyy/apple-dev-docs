# NSDecimalCompare(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Compares two decimal values.

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
func NSDecimalCompare(_ leftOperand: UnsafePointer<Decimal>, _ rightOperand: UnsafePointer<Decimal>) -> ComparisonResult
```

```c
extern NSComparisonResult NSDecimalCompare(const NSDecimal *leftOperand, const NSDecimal *rightOperand);
```

## Return Value

`NSOrderedDescending` if `leftOperand` is bigger than `rightOperand`; `NSOrderedAscending` if `rightOperand` is bigger than `leftOperand`; or `NSOrderedSame` if the two operands are equal.

## Discussion

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Comparing decimals
- [func isEqual(to: Decimal) -> Bool](./decimal/isequal%28to%29.md)
  Indicates whether this decimal is equal to the specified one.
- [func isLess(than: Decimal) -> Bool](./decimal/isless%28than%29.md)
  Indicates whether this decimal is less than the specified one.
- [func isLessThanOrEqualTo(Decimal) -> Bool](./decimal/islessthanorequalto%28_%29.md)
  Indicates whether this decimal is less than or equal to the specified one.
- [func isTotallyOrdered(belowOrEqualTo: Decimal) -> Bool](./decimal/istotallyordered%28beloworequalto%29.md)
  Returns a Boolean value indicating whether this instance should precede the given value in an ascending sort.
- [func distance(to: Decimal) -> Decimal](./decimal/distance%28to%29.md)
  Returns the distance from this value to the specified value.
- [func advanced(by: Decimal) -> Decimal](./decimal/advanced%28by%29.md)
  Returns a new value advanced by the given distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalcompare(_:_:))*