# -(_:_:)

**Framework**: Swift  
**Kind**: op  
**Required**: Yes

Subtracts one value from another and produces their difference, rounded to a representable value.

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
override static func - (lhs: Self, rhs: Self) -> Self
```

#### Discussion

The subtraction operator (`-`) calculates the difference of its two arguments. For example:

```swift
let x = 7.5
let y = x - 2.25
// y == 5.25
```

The `-` operator implements the subtraction operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: A numeric value.
- `rhs`: The value to subtract from `lhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/-(_:_:))*