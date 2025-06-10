# decode(from:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Decodes a value from the provided decoder.

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
static func decode(from decoder: any Decoder) throws -> Self.Value
```

#### Return Value

The decoded value.

#### Discussion

This method throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decodableattributedstringkey/decode(from:))*