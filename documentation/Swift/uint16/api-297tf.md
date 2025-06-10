# ^(_:_:)

**Framework**: Swift  
**Kind**: op

Returns the result of performing a bitwise XOR operation on the two given values.

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
static func ^ (lhs: Self, rhs: Self) -> Self
```

#### Discussion

A bitwise XOR operation, also known as an exclusive OR operation, results in a value that has each bit set to `1` where  of its arguments had that bit set to `1`. For example:

```swift
let x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
let z = x ^ y             // 0b00001011
// z == 11
```

## Parameters

- `lhs`: An integer value.
- `rhs`: Another integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/_(_:_:)-297tf)*