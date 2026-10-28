# setVertexSamplerStates(_:lodMinClamps:lodMaxClamps:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 8.0+
- visionOS

## Declaration

```swift
func setVertexSamplerStates(_ samplers: [(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)
```

## Discussion

Each element of the method’s `lodMinClamps` and `lodMaxClamps` parameters overrides the default values for the corresponding sampler in `samplers`. You can set a sampler’s default values by configuring the [`lodMinClamp`](../mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](../mtlsamplerdescriptor/lodmaxclamp.md) properties of [`MTLSamplerDescriptor`](../mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:`](./setvertexsamplerstates_lodminclamps_lodmaxclamps_withrange_.md).

## Parameters

- `samplers`: An array of [`MTLSamplerState`](../mtlsamplerstate.md) instances the command assigns to entries in the vertex shader argument table for sampler states.
- `lodMinClamps`: An array of floating-point values. Each element is the smallest level of detail value a vertex shader can use when it samples a texture with the corresponding element in `samplers`.
- `lodMaxClamps`: An array of floating-point values. Each element is the largest level of detail value a vertex shader can use when it samples a texture with the corresponding element in `samplers`.
- `range`: A span of integers that represent the entries in the vertex shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## See Also

### Assigning sampler states
- [func setVertexSamplerState((any MTLSamplerState)?, index: Int)](./setvertexsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the vertex shader argument table.
- [func setVertexSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setvertexsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./setvertexsamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates(_:lodminclamps:lodmaxclamps:range:))*