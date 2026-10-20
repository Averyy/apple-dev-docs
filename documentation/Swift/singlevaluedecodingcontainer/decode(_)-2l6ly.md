# decode(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a single value of the given type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func decode(_ type: Int128.Type) throws -> Int128
```

#### Return Value

A value of the requested type.

#### Discussion

> **Throws**: `DecodingError.typeMismatch` if the encountered encoded value cannot be converted to the requested type.

> **Throws**: `DecodingError.valueNotFound` if the encountered encoded value is null.

## Parameters

- `type`: The type to decode as.

## Default Implementations

### SingleValueDecodingContainer Implementations
- [func decode(Int128.Type) throws -> Int128](./decode%28_%29-1rz83.md)
  Decodes a single value of the given type.
- [func decode(Int128.Type) throws -> Int128](./decode%28_%29-5f6dc.md)
  Decodes a single value of the given type.
- [func decode(UInt128.Type) throws -> UInt128](./decode%28_%29-5i4ec.md)
  Decodes a single value of the given type.
- [func decode(UInt128.Type) throws -> UInt128](./decode%28_%29-6vzg2.md)
  Decodes a single value of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevaluedecodingcontainer/decode(_:)-2l6ly)*