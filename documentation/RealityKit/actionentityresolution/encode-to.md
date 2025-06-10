# encode(to:)

**Framework**: RealityKit  
**Kind**: method

Writes the action entity resolution data into an encoder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container. This function throws an [`Error`](https://developer.apple.com/documentation/Swift/Error) if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionentityresolution/encode(to:))*