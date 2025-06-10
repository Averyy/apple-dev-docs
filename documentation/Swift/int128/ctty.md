# &*(_:_:)

**Framework**: Swift  
**Kind**: op

Returns the product of the two given values, wrapping the result in case of any overflow.

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
static func &* (lhs: Self, rhs: Self) -> Self
```

#### Discussion

The overflow multiplication operator (`&*`) discards any bits that overflow the fixed width of the integer type. In the following example, the product of `10` and `50` is greater than the maximum representable `Int8` value, so the result is the partial value after discarding the overflowing bits.

```swift
let x: Int8 = 10 &* 5
// x == 50
let y: Int8 = 10 &* 50
// y == -12 (after overflow)
```

For more about arithmetic with overflow operators, see [`Overflow Operators`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID37) in .

## Parameters

- `lhs`: The first value to multiply.
- `rhs`: The second value to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/&*(_:_:)-ctty)*