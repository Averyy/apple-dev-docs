# +(_:_:)

**Framework**: Swift  
**Kind**: op

Adds two values and produces their sum, rounded to a representable value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func + (lhs: Float80, rhs: Float80) -> Float80
```

#### Discussion

The addition operator (`+`) calculates the sum of its two arguments. For example:

```swift
let x = 1.5
let y = x + 2.25
// y == 3.75
```

The `+` operator implements the addition operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: The first value to add.
- `rhs`: The second value to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/+(_:_:))*