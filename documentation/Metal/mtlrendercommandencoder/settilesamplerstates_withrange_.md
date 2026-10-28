# setTileSamplerStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple sampler states to a range of entries in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```objc
- (void) setTileSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Swift version of this method is [`setTileSamplerStates(_:range:)`](./settilesamplerstates%28_,range%29.md).

## Parameters

- `samplers`: A pointer to a C array of [`MTLSamplerState`](../mtlsamplerstate.md) instances the command assigns to entries in the tile shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the tile shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## See Also

### Assigning sampler states
- [func setTileSamplerState((any MTLSamplerState)?, index: Int)](./settilesamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the tile shader argument table.
- [func setTileSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./settilesamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [- setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./settilesamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstates:withrange:)*