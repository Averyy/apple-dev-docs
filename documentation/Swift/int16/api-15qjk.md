# /=(_:_:)

**Framework**: Swift  
**Kind**: op

Divides the first value by the second and stores the quotient in the left-hand-side variable.

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
static func /= (lhs: inout Int16, rhs: Int16)
```

#### Discussion

For integer types, any remainder of the division is discarded.

```swift
var x = 21
x /= 5
// x == 4
```

## Parameters

- `lhs`: The value to divide.
- `rhs`: The value to divide   by.   must not be zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/_=(_:_:)-15qjk)*