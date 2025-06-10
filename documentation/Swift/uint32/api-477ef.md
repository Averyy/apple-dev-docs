# &>>=(_:_:)

**Framework**: Swift  
**Kind**: op

Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

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
static func &>>= <Other>(lhs: inout Self, rhs: Other) where Other : BinaryInteger
```

#### Discussion

The `&>>=` operator performs a , where the value passed as `rhs` is masked to produce a value in the range `0..<lhs.bitWidth`. The shift is performed using this masked value.

The following example defines `x` as an instance of `UInt8`, an 8-bit, unsigned integer type. If you use `2` as the right-hand-side value in an operation on `x`, the shift amount requires no masking.

```swift
var x: UInt8 = 30                 // 0b00011110
x &>>= 2
// x == 7                         // 0b00000111
```

However, if you use `19` as `rhs`, the operation first bitmasks `rhs` to `3`, and then uses that masked value as the number of bits to shift `lhs`.

```swift
var y: UInt8 = 30                 // 0b00011110
y &>>= 19
// y == 3                         // 0b00000011
```

## Parameters

- `lhs`: The value to shift.
- `rhs`: The number of bits to shift   to the right. If   is   outside the range  , it is masked to produce a   value within that range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/&__=(_:_:)-477ef)*