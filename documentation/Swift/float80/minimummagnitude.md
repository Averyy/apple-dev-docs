# minimumMagnitude(_:_:)

**Framework**: Swift  
**Kind**: method

Returns the value with lesser magnitude.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func minimumMagnitude(_ x: Self, _ y: Self) -> Self
```

#### Return Value

Whichever of `x` or `y` has lesser magnitude, or whichever is a number if the other is NaN.

#### Discussion

This method returns the value with lesser magnitude of the two given values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `minimumMagnitude(x, y)` is `x` if `x.magnitude <= y.magnitude`, `y` if `y.magnitude < x.magnitude`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.minimumMagnitude(10.0, -25.0)
// 10.0
Double.minimumMagnitude(10.0, .nan)
// 10.0
Double.minimumMagnitude(.nan, -25.0)
// -25.0
Double.minimumMagnitude(.nan, .nan)
// nan
```

The `minimumMagnitude` method implements the `minNumMag` operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `x`: A floating-point value.
- `y`: Another floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/minimummagnitude(_:_:))*