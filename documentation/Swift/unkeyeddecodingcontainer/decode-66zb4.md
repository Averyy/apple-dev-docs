# decode(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a value of the given type.

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
mutating func decode(_ type: UInt128.Type) throws -> UInt128
```

#### Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> **Note**: `DecodingError.valueNotFound` if the encountered encoded value is null, or of there are no more values to decode.

## Parameters

- `type`: The type of value to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decode(_:)-66zb4)*