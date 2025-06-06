# encodeNil()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes a null value.

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
mutating func encodeNil() throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if a null value is invalid in the current context for this format.

`EncodingError.invalidValue` if a null value is invalid in the current context for this format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodenil())*