# &*(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator  
**Required**: Yes

Returns the product of the two given values, wrapping the result in case of any overflow.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

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

For more about arithmetic with overflow operators, see [Overflow Operators](https://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID37) in *[The Swift Programming Language](https://docs.swift.org/swift-book/)*.

## Parameters

- `lhs`: The first value to multiply.
- `rhs`: The second value to multiply.

## Default Implementations

### FixedWidthInteger Implementations
- [static func &* (Self, Self) -> Self](./ampstar%28_,_%29-8uc7d.md)
  Returns the product of the two given values, wrapping the result in case of any overflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fixedwidthinteger/&*(_:_:))*