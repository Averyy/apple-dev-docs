# max

**Framework**: Swift  
**Kind**: property

The maximum representable integer in this type.

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
static var max: Int128 { get }
```

#### Discussion

For unsigned integer types, this value is `(2 ** bitWidth) - 1`, where `**` is exponentiation. For signed integer types, this value is `(2 ** (bitWidth - 1)) - 1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/max)*