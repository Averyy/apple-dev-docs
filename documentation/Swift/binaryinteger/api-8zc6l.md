# /(_:_:)

**Framework**: Swift  
**Kind**: op  
**Required**: Yes

Returns the quotient of dividing the first value by the second.

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
static func / (lhs: Self, rhs: Self) -> Self
```

#### Discussion

For integer types, any remainder of the division is discarded.

```swift
let x = 21 / 5
// x == 4
```

## Parameters

- `lhs`: The value to divide.
- `rhs`: The value to divide   by.   must not be zero.

## See Also

- [static func + (Self, Self) -> Self](binaryinteger/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Self, Self) -> Self](binaryinteger/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func * (Self, Self) -> Self](binaryinteger/*(_:_:).md)
  Multiplies two values and produces their product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/_(_:_:)-8zc6l)*