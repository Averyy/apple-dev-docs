# ~(_:)

**Framework**: Swift  
**Kind**: op  
**Required**: Yes

Returns the inverse of the bits set in the argument.

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
static func ~ (x: Self) -> Self
```

#### Discussion

The bitwise NOT operator (`~`) is a prefix operator that returns a value in which all the bits of its argument are flipped: Bits that are `1` in the argument are `0` in the result, and bits that are `0` in the argument are `1` in the result. This is equivalent to the inverse of a set. For example:

```swift
let x: UInt8 = 5        // 0b00000101
let notX = ~x           // 0b11111010
```

Performing a bitwise NOT operation on 0 returns a value with every bit set to `1`.

```swift
let allOnes = ~UInt8.min   // 0b11111111
```

> **Note**: O(1).

## See Also

- [static func & (Self, Self) -> Self](binaryinteger/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout Self, Self)](binaryinteger/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/~(_:))*