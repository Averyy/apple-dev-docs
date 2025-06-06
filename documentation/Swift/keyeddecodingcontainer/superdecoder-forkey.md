# superDecoder(forKey:)

**Framework**: Swift  
**Kind**: method

Returns a `Decoder` instance for decoding `super` from the container associated with the given key.

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
func superDecoder(forKey key: KeyedDecodingContainer<K>.Key) throws -> any Decoder
```

#### Return Value

A new `Decoder` to pass to `super.init(from:)`.

#### Discussion

> **Note**: `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

> **Note**: `DecodingError.valueNotFound` if `self` has a null entry for the given key.

## Parameters

- `key`: The key to decode   for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainer/superdecoder(forkey:))*