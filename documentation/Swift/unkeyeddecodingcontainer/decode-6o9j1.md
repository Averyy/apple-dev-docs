# decode(_:)

**Framework**: Swift  
**Kind**: method  
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
mutating func decode(_ type: Int64.Type) throws -> Int64
```

#### Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> **Note**: `DecodingError.valueNotFound` if the encountered encoded value is null, or of there are no more values to decode.

## Parameters

- `type`: The type of value to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decode(_:)-6o9j1)*