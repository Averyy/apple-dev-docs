# setVertexSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a sampler state to an entry in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setVertexSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

```objc
- (void) setVertexSamplerState:(id<MTLSamplerState>) sampler atIndex:(NSUInteger) index;
```

## Discussion

By default, the sampler state at each index is `nil`.

## Parameters

- `sampler`: An [`MTLSamplerState`](../mtlsamplerstate.md) instance the command assigns to an entry in the vertex shader argument table for sampler states.
- `index`: An integer that represents the entry in the vertex shader argument table for sampler states that stores a record of `sampler`.

## See Also

### Assigning sampler states
- [func setVertexSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setvertexsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./setvertexsamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./setvertexsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.
- [- setVertexSamplerStates:withRange:](./setvertexsamplerstates_withrange_.md)
  Assigns multiple sampler states to a range of entries in the vertex shader argument table.
- [- setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./setvertexsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexsamplerstate(_:index:))*