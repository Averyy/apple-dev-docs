# isLessThanOrEqualTo(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether this instance is less than or equal to the given value.

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
func isLessThanOrEqualTo(_ other: Self) -> Bool
```

#### Return Value

`true` if `other` is greater than this value; otherwise, `false`. If either this value or `other` is NaN, the result of this method is `false`.

#### Discussion

This method serves as the basis for the less-than-or-equal-to operator (`<=`) for floating-point values. Some special cases apply:

- Because NaN is incomparable with any value, this method returns `false` when called on NaN or when NaN is passed as `other`.
- `-infinity` compares less than or equal to all values except NaN.
- Every value except NaN compares less than or equal to `+infinity`.

The following example shows the behavior of the `isLessThanOrEqualTo(_:)` method with different kinds of values:

```swift
let x = 15.0
x.isLessThanOrEqualTo(20.0)
// true
x.isLessThanOrEqualTo(.nan)
// false
Double.nan.isLessThanOrEqualTo(x)
// false
```

The `isLessThanOrEqualTo(_:)` method implements the less-than-or-equal predicate defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `other`: The value to compare with this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/islessthanorequalto(_:))*