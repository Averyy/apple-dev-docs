# *=(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Multiplies two values and stores the result in the left-hand-side variable.

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
static func *= (lhs: inout Int64, rhs: Int64)
```

## Discussion

The product of the two arguments must be representable in the arguments’ type. In the following example, the result of `21 * 21` is greater than the maximum representable `Int8` value:

```swift
var x: Int8 = 21
x *= 21
// Overflow error
```

> **Note**: Overflow checking is not performed in `-Ounchecked` builds.

## Parameters

- `lhs`: The first value to multiply.
- `rhs`: The second value to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int64/*=(_:_:))*