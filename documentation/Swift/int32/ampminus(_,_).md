# &-(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns the difference of the two given values, wrapping the result in case of any overflow.

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
static func &- (lhs: Self, rhs: Self) -> Self
```

## Discussion

The overflow subtraction operator (`&-`) discards any bits that overflow the fixed width of the integer type. In the following example, the difference of `10` and `21` is less than zero, the minimum representable `UInt` value, so the result is the partial value after discarding the overflowing bits.

```swift
let x: UInt8 = 21 &- 10
// x == 11
let y: UInt8 = 10 &- 21
// y == 245 (after overflow)
```

For more about arithmetic with overflow operators, see [Overflow Operators](https://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID37) in *[The Swift Programming Language](https://docs.swift.org/swift-book/)*.

## Parameters

- `lhs`: A numeric value.
- `rhs`: The value to subtract from `lhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/&-(_:_:))*