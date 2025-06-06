# nestedContainer(keyedBy:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a nested container keyed by the given type.

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
mutating func nestedContainer<NestedKey>(keyedBy type: NestedKey.Type) throws -> KeyedDecodingContainer<NestedKey> where NestedKey : CodingKey
```

#### Return Value

A keyed decoding container view into `self`.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered stored value is not a keyed container.

## Parameters

- `type`: The key type to use for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/nestedcontainer(keyedby:))*