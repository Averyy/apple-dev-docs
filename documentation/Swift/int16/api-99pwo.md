# &<<=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

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
static func &<<= (lhs: inout Int16, rhs: Int16)
```

#### Discussion

The `&<<=` operator performs a , where the value used as `rhs` is masked to produce a value in the range `0..<lhs.bitWidth`. The shift is performed using this masked value.

The following example defines `x` as an instance of `UInt8`, an 8-bit, unsigned integer type. If you use `2` as the right-hand-side value in an operation on `x`, the shift amount requires no masking.

```swift
var x: UInt8 = 30                 // 0b00011110
x &<<= 2
// x == 120                       // 0b01111000
```

However, if you pass `19` as `rhs`, the method first bitmasks `rhs` to `3`, and then uses that masked value as the number of bits to shift `lhs`.

```swift
var y: UInt8 = 30                 // 0b00011110
y &<<= 19
// y == 240                       // 0b11110000
```

## Parameters

- `lhs`: The value to shift.
- `rhs`: The number of bits to shift   to the left. If   is   outside the range  , it is masked to produce a   value within that range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/&__=(_:_:)-99pwo)*