# setVertexSamplerState(_:lodMinClamp:lodMaxClamp:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a sampler state and clamp values to an entry in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setVertexSamplerState(_ sampler: (any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)
```

#### Discussion

The method’s `lodMinClamp` and `lodMaxClamp` parameters override the default values for `sampler`. You can set the sampler’s default values by configuring the [`lodMinClamp`](mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](mtlsamplerdescriptor/lodmaxclamp.md) properties of [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

## Parameters

- `sampler`: An   instance the command assigns to an entry in the vertex shader argument table for sampler states.
- `lodMinClamp`: The smallest level of detail value a vertex shader can use when it samples a texture.
- `lodMaxClamp`: The largest level of detail value a vertex shader can use when it samples a texture.
- `index`: An integer that represents the entry in the vertex shader argument table for sampler states that stores a record of  .

## See Also

- [func setVertexSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setvertexsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setvertexsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setvertexsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexsamplerstate(_:lodminclamp:lodmaxclamp:index:))*