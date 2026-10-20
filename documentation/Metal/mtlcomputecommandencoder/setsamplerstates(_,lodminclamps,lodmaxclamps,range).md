# setSamplerStates(_:lodMinClamps:lodMaxClamps:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 8.0+
- visionOS

## Declaration

```swift
func setSamplerStates(_ samplers: [(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)
```

#### Discussion

> ❗ **Important**:  This method requires that the lengths of `samplers`, `lodMinClamps`, and `lodMaxClamps` be the same as the length of `range`.

Calling this method ignores the [`lodMinClamp`](../mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](../mtlsamplerdescriptor/lodmaxclamp.md) properties of the samplers, using the provided levels of detail instead.

## Parameters

- `samplers`: A list of [`MTLSamplerState`](../mtlsamplerstate.md) instances to bind to the sampler argument table.
- `lodMinClamps`: An array of minimum levels of detail to use for the corresponding sampler in `samplers`.
- `lodMaxClamps`: An array of maximum levels of detail to use for the corresponding sample in `samplers`.
- `range`: A range of indices in the sampler state argument table.

## See Also

### Binding texture samplers
- [func setSamplerState((any MTLSamplerState)?, index: Int)](./setsamplerstate%28_,index%29.md)
  Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./setsamplerstates%28_,range%29.md)
  Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstates(_:lodminclamps:lodmaxclamps:range:))*