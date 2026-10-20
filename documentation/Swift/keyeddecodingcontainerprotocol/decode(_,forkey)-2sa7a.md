# decode(_:forKey:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a value of the given type for the given key.

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
func decode(_ type: Int128.Type, forKey key: Self.Key) throws -> Int128
```

#### Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

#### Discussion

> **Throws**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> **Throws**: `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

> **Throws**: `DecodingError.valueNotFound` if `self` has a null entry for the given key.

## Parameters

- `type`: The type of value to decode.
- `key`: The key that the decoded value is associated with.

## Default Implementations

### KeyedDecodingContainerProtocol Implementations
- [func decode(Int128.Type, forKey: Self.Key) throws -> Int128](./decode%28_,forkey%29-7za3v.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt128.Type, forKey: Self.Key) throws -> UInt128](./decode%28_,forkey%29-u839.md)
  Decodes a value of the given type for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decode(_:forkey:)-2sa7a)*