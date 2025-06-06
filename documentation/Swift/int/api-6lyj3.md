# %(_:_:)

**Framework**: Swift  
**Kind**: op

Returns the remainder of dividing the first value by the second.

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
static func % (lhs: Int, rhs: Int) -> Int
```

#### Discussion

The result of the remainder operator (`%`) has the same sign as `lhs` and has a magnitude less than `rhs.magnitude`.

```swift
let x = 22 % 5
// x == 2
let y = 22 % -5
// y == 2
let z = -22 % -5
// z == -2
```

For any two integers `a` and `b`, their quotient `q`, and their remainder `r`, `a == b * q + r`.

## Parameters

- `lhs`: The value to divide.
- `rhs`: The value to divide   by.   must not be zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/_(_:_:)-6lyj3)*