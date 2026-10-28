# -(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Subtracts one value from another and produces their difference, rounded to a representable value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func - (lhs: Float80, rhs: Float80) -> Float80
```

## Discussion

The subtraction operator (`-`) calculates the difference of its two arguments. For example:

```swift
let x = 7.5
let y = x - 2.25
// y == 5.25
```

The `-` operator implements the subtraction operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: A numeric value.
- `rhs`: The value to subtract from `lhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/-(_:_:))*