# encode(to:configuration:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Encodes the value into the specified encoder with help from the provided configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func encode(to encoder: any Encoder, configuration: Self.EncodingConfiguration) throws
```

## Parameters

- `encoder`: The encoder to write data to.
- `configuration`: An encoding configuration instance that provides additional information necessary for encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodablewithconfiguration/encode(to:configuration:))*