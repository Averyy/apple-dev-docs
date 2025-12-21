# bigEndian

**Framework**: Network  
**Kind**: property  
**Required**: Yes

The big-endian representation of this integer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
override var bigEndian: Self { get }
```

#### Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkfixedwidthinteger/bigendian)*