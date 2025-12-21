# decode(_:from:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Decode a decodable object from Data

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
func decode<T>(_ type: T.Type, from data: Data) throws -> T where T : Decodable
```

#### Return Value

An instance of type T or throws an error if unable to decode.

## Parameters

- `type`: The type to decode into.
- `data`: The data to use for decoding


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkdecoder/decode(_:from:))*