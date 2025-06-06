# -=(_:_:)

**Framework**: Swift  
**Kind**: op

Subtracts the second value from the first and stores the difference in the left-hand-side variable.

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
static func -= (lhs: inout Int, rhs: Int)
```

#### Discussion

The difference of the two arguments must be representable in the arguments’ type. In the following example, the result of `21 - 50` is less than zero, the minimum representable `UInt8` value:

```swift
var x: UInt8 = 21
x -= 50
// Overflow error
```

> **Note**: Overflow checking is not performed in `-Ounchecked` builds.

Overflow checking is not performed in `-Ounchecked` builds.

## Parameters

- `lhs`: A numeric value.
- `rhs`: The value to subtract from  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/-=(_:_:))*