# setSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a sampler into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler`: A sampler the method encodes.
- `index`: The index of a sampler within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlargumentencoder/setsamplerstates(_:range:).md)
  Encodes an array of samplers into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstate(_:index:))*