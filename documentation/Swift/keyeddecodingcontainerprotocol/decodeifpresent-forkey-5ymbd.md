# decodeIfPresent(_:forKey:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a value of the given type for the given key, if present.

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
func decodeIfPresent(_ type: UInt8.Type, forKey key: Self.Key) throws -> UInt8?
```

#### Return Value

A decoded value of the requested type, or `nil` if the `Decoder` does not have an entry associated with the given key, or if the value is a null value.

#### Discussion

This method returns `nil` if the container does not have a value associated with `key`, or if the value is null. The difference between these states can be distinguished with a `contains(_:)` call.

> **Note**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

`DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

## Parameters

- `type`: The type of value to decode.
- `key`: The key that the decoded value is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-5ymbd)*