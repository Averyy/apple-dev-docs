# encode(to:)

**Framework**: Swift  
**Kind**: method

Encodes the contents of this dictionary into the given encoder.

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
func encode(to encoder: any Encoder) throws
```

#### Discussion

If the dictionary uses keys that are `String`, `Int`, or a type conforming to `CodingKeyRepresentable`, the contents are encoded in a keyed container. Otherwise, the contents are encoded as alternating key-value pairs in an unkeyed container.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [init(from: any Decoder) throws](dictionary/init(from:)-6e6js.md)
  Creates a new dictionary by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/encode(to:))*