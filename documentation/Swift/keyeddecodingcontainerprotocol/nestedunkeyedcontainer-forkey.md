# nestedUnkeyedContainer(forKey:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns the data stored for the given key as represented in an unkeyed container.

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
func nestedUnkeyedContainer(forKey key: Self.Key) throws -> any UnkeyedDecodingContainer
```

#### Return Value

An unkeyed decoding container view into `self`.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered stored value is not an unkeyed container.

`DecodingError.typeMismatch` if the encountered stored value is not an unkeyed container.

## Parameters

- `key`: The key that the nested container is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/nestedunkeyedcontainer(forkey:))*