# encode(_:to:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Encodes a value to the provided encoder.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func encode(_ value: Self.Value, to encoder: any Encoder) throws
```

#### Discussion

This method throws an error if writing to the encoder fails.

## Parameters

- `value`: The value to encode.
- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodableattributedstringkey/encode(_:to:))*