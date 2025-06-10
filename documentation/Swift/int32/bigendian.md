# bigEndian

**Framework**: Swift  
**Kind**: property

The big-endian representation of this integer.

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
var bigEndian: Self { get }
```

#### Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/bigendian)*