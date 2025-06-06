# decode(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a single value of the given type.

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
func decode(_ type: Int16.Type) throws -> Int16
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevaluedecodingcontainer/decode(_:)-23u3w)*