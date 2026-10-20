# /(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns the quotient of dividing the first value by the second, rounded to a representable value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static func / (lhs: Float16, rhs: Float16) -> Float16
```

#### Discussion

The division operator (`/`) calculates the quotient of the division if `rhs` is nonzero. If `rhs` is zero, the result of the division is infinity, with the sign of the result matching the sign of `lhs`.

```swift
let x = 16.875
let y = x / 2.25
// y == 7.5

let z = x / 0
// z.isInfinite == true
```

The `/` operator implements the division operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: The value to divide.
- `rhs`: The value to divide `lhs` by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/_(_:_:))*