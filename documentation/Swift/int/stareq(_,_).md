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
static func *= (lhs: inout Int, rhs: Int)
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

## See Also

### Arithmetic with Assignment
- [static func += (inout Int, Int)](./pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func /= (inout Int, Int)](./opeq%28_,_%29-9lzpe.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/*=(_:_:))*