# encode(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes the given value.

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
mutating func encode(_ value: Int) throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

`EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:)-30ux3)*