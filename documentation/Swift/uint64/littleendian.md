# littleEndian

**Framework**: Swift  
**Kind**: property

The little-endian representation of this integer.

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
var littleEndian: Self { get }
```

#### Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a little-endian platform, for any integer `x`, `x == x.littleEndian`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/littleendian)*