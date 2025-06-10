# bigEndian

**Framework**: Network  
**Kind**: property  
**Required**: Yes

The big-endian representation of this integer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
override var bigEndian: Self { get }
```

#### Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkfixedwidthinteger/bigendian)*