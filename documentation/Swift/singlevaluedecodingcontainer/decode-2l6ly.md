# decode(_:)

**Framework**: Swift  
**Kind**: method  
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

> **Note**: `DecodingError.typeMismatch` if the encountered encoded value cannot be converted to the requested type.

`DecodingError.typeMismatch` if the encountered encoded value cannot be converted to the requested type.

> **Note**: `DecodingError.valueNotFound` if the encountered encoded value is null.

`DecodingError.valueNotFound` if the encountered encoded value is null.

## Parameters

- `type`: The type to decode as.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevaluedecodingcontainer/decode(_:)-2l6ly)*