# transcode(_:from:)

**Framework**: Swift  
**Kind**: method

Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.

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
static func transcode<FromEncoding>(_ content: FromEncoding.EncodedScalar, from _: FromEncoding.Type) -> Unicode.ASCII.EncodedScalar? where FromEncoding : _UnicodeEncoding
```

#### Discussion

A default implementation of this method will be provided automatically for any conforming type that does not implement one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/ascii/transcode(_:from:))*