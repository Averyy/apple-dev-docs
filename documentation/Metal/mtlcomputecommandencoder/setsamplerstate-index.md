# setSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler`: An   instance to bind to the sampler argument table.
- `index`: The index in the sampler argument table to bind the sampler to.

## See Also

- [func setSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlcomputecommandencoder/setsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlcomputecommandencoder/setsamplerstates(_:range:).md)
  Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlcomputecommandencoder/setsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstate(_:index:))*