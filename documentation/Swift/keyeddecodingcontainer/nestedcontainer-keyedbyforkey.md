# nestedContainer(keyedBy:forKey:)

**Framework**: Swift  
**Kind**: method

Returns the data stored for the given key as represented in a container keyed by the given key type.

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
func nestedContainer<NestedKey>(keyedBy type: NestedKey.Type, forKey key: KeyedDecodingContainer<K>.Key) throws -> KeyedDecodingContainer<NestedKey> where NestedKey : CodingKey
```

#### Return Value

A keyed decoding container view into `self`.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered stored value is not a keyed container.

`DecodingError.typeMismatch` if the encountered stored value is not a keyed container.

## Parameters

- `type`: The key type to use for the container.
- `key`: The key that the nested container is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainer/nestedcontainer(keyedby:forkey:))*