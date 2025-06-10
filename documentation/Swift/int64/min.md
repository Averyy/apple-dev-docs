# min

**Framework**: Swift  
**Kind**: property

The minimum representable integer in this type.

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
static var min: Self { get }
```

#### Discussion

For signed integer types, this value is `-(2 ** (bitWidth - 1))`, where `**` is exponentiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int64/min)*