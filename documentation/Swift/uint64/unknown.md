# &-=(_:_:)

**Framework**: Swift  
**Kind**: op

Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.

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
static func &-= (lhs: inout Self, rhs: Self)
```

#### Discussion

The masking subtraction assignment operator (`&-=`) silently wraps any overflow that occurs during the operation. In the following example, the difference of `10` and `21` is less than zero, the minimum representable `UInt` value, so the result is the result is the partial value after discarding the overflowing bits.

```swift
var x: Int8 = 21
x &-= 10
// x == 11
var y: UInt8 = 10
y &-= 21
// y == 245 (after overflow)
```

For more about arithmetic with overflow operators, see [`Overflow Operators`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID37) in .

## Parameters

- `lhs`: A numeric value.
- `rhs`: The value to subtract from  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/&-=(_:_:))*