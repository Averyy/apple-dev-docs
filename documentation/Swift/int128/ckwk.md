# ^=(_:_:)

**Framework**: Swift  
**Kind**: op

Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func ^= (a: inout Int128, b: Int128)
```

#### Discussion

A bitwise XOR operation, also known as an exclusive OR operation, results in a value that has each bit set to `1` where  of its arguments had that bit set to `1`. For example:

```swift
var x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
x ^= y                    // 0b00001011
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/_=(_:_:)-ckwk)*