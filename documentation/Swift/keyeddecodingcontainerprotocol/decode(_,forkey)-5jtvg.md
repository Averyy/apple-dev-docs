# decode(_:forKey:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a value of the given type for the given key.

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
func decode(_ type: Int32.Type, forKey key: Self.Key) throws -> Int32
```

#### Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> **Note**: `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

> **Note**: `DecodingError.valueNotFound` if `self` has a null entry for the given key.

## Parameters

- `type`: The type of value to decode.
- `key`: The key that the decoded value is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decode(_:forkey:)-5jtvg)*