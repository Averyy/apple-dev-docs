# setSamplerStates(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes an array of samplers into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func setSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers`: An array of samplers the method encodes.
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setSamplerState((any MTLSamplerState)?, index: Int)](mtlargumentencoder/setsamplerstate(_:index:).md)
  Encodes a sampler into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstates(_:range:))*