# maximum(_:_:)

**Framework**: Swift  
**Kind**: method

Returns the greater of the two given values.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func maximum(_ x: Self, _ y: Self) -> Self
```

#### Return Value

The greater of `x` and `y`, or whichever is a number if the other is NaN.

#### Discussion

This method returns the maximum of two values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `maximum(x, y)` is `x` if `x > y`, `y` if `x <= y`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.maximum(10.0, -25.0)
// 10.0
Double.maximum(10.0, .nan)
// 10.0
Double.maximum(.nan, -25.0)
// -25.0
Double.maximum(.nan, .nan)
// nan
```

The `maximum` method implements the `maxNum` operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `x`: A floating-point value.
- `y`: Another floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/maximum(_:_:))*