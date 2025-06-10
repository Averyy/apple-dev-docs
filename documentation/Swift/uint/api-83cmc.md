# &>>(_:_:)

**Framework**: Swift  
**Kind**: op

Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.

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
static func &>> (lhs: UInt, rhs: UInt) -> UInt
```

#### Discussion

Use the masking right shift operator (`&>>`) when you need to perform a shift and are sure that the shift amount is in the range `0..<lhs.bitWidth`. Before shifting, the masking right shift operator masks the shift to this range. The shift is performed using this masked value.

The following example defines `x` as an instance of `UInt8`, an 8-bit, unsigned integer type. If you use `2` as the right-hand-side value in an operation on `x`, the shift amount requires no masking.

```swift
let x: UInt8 = 30                 // 0b00011110
let y = x &>> 2
// y == 7                         // 0b00000111
```

However, if you use `8` as the shift amount, the method first masks the shift amount to zero, and then performs the shift, resulting in no change to the original value.

```swift
let z = x &>> 8
// z == 30                        // 0b00011110
```

If the bit width of the shifted integer type is a power of two, masking is performed using a bitmask; otherwise, masking is performed using a modulo operation.

## Parameters

- `lhs`: The value to shift.
- `rhs`: The number of bits to shift   to the right. If   is   outside the range  , it is masked to produce a   value within that range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint/&__(_:_:)-83cmc)*