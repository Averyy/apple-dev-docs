# maximumMagnitude(_:_:)

**Framework**: Swift  
**Kind**: method

Returns the value with greater magnitude.

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
static func maximumMagnitude(_ x: Self, _ y: Self) -> Self
```

#### Return Value

Whichever of `x` or `y` has greater magnitude, or whichever is a number if the other is NaN.

#### Discussion

This method returns the value with greater magnitude of the two given values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `maximumMagnitude(x, y)` is `x` if `x.magnitude > y.magnitude`, `y` if `x.magnitude <= y.magnitude`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.maximumMagnitude(10.0, -25.0)
// -25.0
Double.maximumMagnitude(10.0, .nan)
// 10.0
Double.maximumMagnitude(.nan, -25.0)
// -25.0
Double.maximumMagnitude(.nan, .nan)
// nan
```

The `maximumMagnitude` method implements the `maxNumMag` operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `x`: A floating-point value.
- `y`: Another floating-point value.

## See Also

- [Floating-Point Operators for Float](floating-point-operators-for-float.md)
  Perform arithmetic and bitwise operations or compare values.
- [func isEqual(to: Float) -> Bool](float/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Float) -> Bool](float/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Float) -> Bool](float/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](float/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [static func maximum(Self, Self) -> Self](float/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func minimum(Self, Self) -> Self](float/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](float/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/maximummagnitude(_:_:))*