# *(_:_:)

**Framework**: Swift  
**Kind**: op

Multiplies two values and produces their product, rounding to a representable value.

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
static func * (lhs: Double, rhs: Double) -> Double
```

#### Discussion

The multiplication operator (`*`) calculates the product of its two arguments. For example:

```swift
let x = 7.5
let y = x * 2.25
// y == 16.875
```

The `*` operator implements the multiplication operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: The first value to multiply.
- `rhs`: The second value to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/*(_:_:))*