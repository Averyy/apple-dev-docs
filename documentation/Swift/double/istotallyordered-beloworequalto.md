# isTotallyOrdered(belowOrEqualTo:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.

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
func isTotallyOrdered(belowOrEqualTo other: Self) -> Bool
```

#### Return Value

`true` if this value is ordered below or the same as `other` in a total ordering of the floating-point type; otherwise, `false`.

#### Discussion

This relation is a refinement of the less-than-or-equal-to operator (`<=`) that provides a total order on all values of the type, including signed zeros and NaNs.

The following example uses `isTotallyOrdered(belowOrEqualTo:)` to sort an array of floating-point values, including some that are NaN:

```swift
var numbers = [2.5, 21.25, 3.0, .nan, -9.5]
numbers.sort { !$1.isTotallyOrdered(belowOrEqualTo: $0) }
print(numbers)
// Prints "[-9.5, 2.5, 3.0, 21.25, nan]"
```

The `isTotallyOrdered(belowOrEqualTo:)` method implements the total order relation as defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `other`: A floating-point value to compare to this value.

## See Also

- [Floating-Point Operators for Double](floating-point-operators-for-double.md)
  Perform arithmetic and bitwise operations or compare values.
- [func isEqual(to: Double) -> Bool](double/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Double) -> Bool](double/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Double) -> Bool](double/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [static func minimum(Self, Self) -> Self](double/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](double/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.
- [static func maximum(Self, Self) -> Self](double/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](double/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/istotallyordered(beloworequalto:))*