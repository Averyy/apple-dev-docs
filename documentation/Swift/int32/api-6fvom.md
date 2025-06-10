# /(_:_:)

**Framework**: Swift  
**Kind**: op

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
static func / (lhs: Int32, rhs: Int32) -> Int32
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/_(_:_:)-6fvom)*