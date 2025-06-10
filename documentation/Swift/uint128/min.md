# min

**Framework**: Swift  
**Kind**: property

The minimum representable integer in this type.

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
static var min: UInt128 { get }
```

#### Discussion

For unsigned integer types, this value is always `0`. For signed integer types, this value is `-(2 ** (bitWidth - 1))`, where `**` is exponentiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/min)*