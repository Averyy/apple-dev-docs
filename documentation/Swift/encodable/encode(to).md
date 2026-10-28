# encode(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes this value into the given encoder.

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

## Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## Default Implementations

### Encodable Implementations
- [func encode(to: any Encoder) throws](./encode%28to%29-4qkz3.md)
  Encodes the scalars of this vector into the given encoder in an unkeyed container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encodable/encode(to:))*