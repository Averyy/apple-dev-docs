# singleValueContainer()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns the data stored in this decoder as represented in a container appropriate for holding a single primitive value.

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
func singleValueContainer() throws -> any SingleValueDecodingContainer
```

#### Return Value

A single value container view into this decoder.

#### Discussion

> **Note**: `DecodingError.typeMismatch` if the encountered stored value is not a single value container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decoder/singlevaluecontainer())*