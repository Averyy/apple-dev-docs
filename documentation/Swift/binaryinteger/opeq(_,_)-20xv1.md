# /=(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator  
**Required**: Yes

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
static func /= (lhs: inout Self, rhs: Self)
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
- `rhs`: The value to divide `lhs` by. `rhs` must not be zero.

## See Also

### Arithmetic with Assignment
- [static func += (inout Self, Self)](./pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout Self, Self)](./minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func *= (inout Self, Self)](./stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/_=(_:_:)-20xv1)*