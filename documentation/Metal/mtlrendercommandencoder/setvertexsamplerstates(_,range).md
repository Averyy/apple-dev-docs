# setVertexSamplerStates(_:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple sampler states to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 8.0+
- visionOS

## Declaration

```swift
func setVertexSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setVertexSamplerStates:withRange:`](./setvertexsamplerstates_withrange_.md).

## Parameters

- `samplers`: An array of [`MTLSamplerState`](../mtlsamplerstate.md) instances the command assigns to entries in the vertex shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the vertex shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## See Also

### Assigning sampler states
- [func setVertexSamplerState((any MTLSamplerState)?, index: Int)](./setvertexsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the vertex shader argument table.
- [func setVertexSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setvertexsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./setvertexsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates(_:range:))*