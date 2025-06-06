# container(keyedBy:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns the data stored in this decoder as represented in a container keyed by the given key type.

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
func container<Key>(keyedBy type: Key.Type) throws -> KeyedDecodingContainer<Key> where Key : CodingKey
```

#### Return Value

A keyed decoding container view into this decoder.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered stored value is not a keyed container.

## Parameters

- `type`: The key type to use for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decoder/container(keyedby:))*