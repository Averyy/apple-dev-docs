# <<=(_:_:)

**Framework**: Swift  
**Kind**: op

Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.

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
static func <<= <Other>(lhs: inout Self, rhs: Other) where Other : BinaryInteger
```

#### Discussion

The `<<` operator performs a , which defines a result for a shift of any value.

- Using a negative value for `rhs` performs a right shift using `abs(rhs)`.
- Using a value for `rhs` that is greater than or equal to the bit width of `lhs` is an , resulting in zero.
- Using any other value for `rhs` performs a left shift on `lhs` by that amount.

The following example defines `x` as an instance of `UInt8`, an 8-bit, unsigned integer type. If you use `2` as the right-hand-side value in an operation on `x`, the value is shifted left by two bits.

```swift
var x: UInt8 = 30                 // 0b00011110
x <<= 2
// x == 120                       // 0b01111000
```

If you use `11` as `rhs`, `x` is overshifted such that all of its bits are set to zero.

```swift
var y: UInt8 = 30                 // 0b00011110
y <<= 11
// y == 0                         // 0b00000000
```

Using a negative value as `rhs` is the same as performing a right shift with `abs(rhs)`.

```swift
var a: UInt8 = 30                 // 0b00011110
a <<= -3
// a == 3                         // 0b00000011

var b: UInt8 = 30                 // 0b00011110
b >>= 3
// b == 3                         // 0b00000011
```

## Parameters

- `lhs`: The value to shift.
- `rhs`: The number of bits to shift   to the left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/__=(_:_:)-7usr)*