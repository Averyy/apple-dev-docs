# decode(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a value of the given type.

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
mutating func decode<T>(_ type: T.Type) throws -> T where T : Decodable
```

## Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

## Discussion

> **Throws**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> **Throws**: `DecodingError.valueNotFound` if the encountered encoded value is null, or of there are no more values to decode.

## Parameters

- `type`: The type of value to decode.

## Default Implementations

### UnkeyedDecodingContainer Implementations
- [func decode(UInt128.Type) throws -> UInt128](./decode%28_%29-4c0se.md)
  Decodes a value of the given type.
- [func decode(Int128.Type) throws -> Int128](./decode%28_%29-6k8gu.md)
  Decodes a value of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decode(_:)-2jd5t)*