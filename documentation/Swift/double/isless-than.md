# isLess(than:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether this instance is less than the given value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isLess(than other: Double) -> Bool
```

#### Return Value

`true` if this value is less than `other`; otherwise, `false`. If either this value or `other` is NaN, the result of this method is `false`.

#### Discussion

This method serves as the basis for the less-than operator (`<`) for floating-point values. Some special cases apply:

- Because NaN compares not less than nor greater than any value, this method returns `false` when called on NaN or when NaN is passed as `other`.
- `-infinity` compares less than all values except for itself and NaN.
- Every value except for NaN and `+infinity` compares less than `+infinity`.

The following example shows the behavior of the `isLess(than:)` method with different kinds of values:

```swift
let x = 15.0
x.isLess(than: 20.0)
// true
x.isLess(than: .nan)
// false
Double.nan.isLess(than: x)
// false
```

The `isLess(than:)` method implements the less-than predicate defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `other`: The value to compare with this value.

## See Also

- [Floating-Point Operators for Double](floating-point-operators-for-double.md)
  Perform arithmetic and bitwise operations or compare values.
- [func isEqual(to: Double) -> Bool](double/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLessThanOrEqualTo(Double) -> Bool](double/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](double/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [static func minimum(Self, Self) -> Self](double/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](double/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.
- [static func maximum(Self, Self) -> Self](double/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](double/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/isless(than:))*