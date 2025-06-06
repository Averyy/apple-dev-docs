# encode(to:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `Int64`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype/value/encode(to:))*