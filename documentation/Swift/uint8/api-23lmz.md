# ^=(_:_:)

**Framework**: Swift  
**Kind**: op

Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.

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
static func ^= (lhs: inout UInt8, rhs: UInt8)
```

#### Discussion

A bitwise XOR operation, also known as an exclusive OR operation, results in a value that has each bit set to `1` where  of its arguments had that bit set to `1`. For example:

```swift
var x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
x ^= y                    // 0b00001011
```

## Parameters

- `lhs`: An integer value.
- `rhs`: Another integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/_=(_:_:)-23lmz)*