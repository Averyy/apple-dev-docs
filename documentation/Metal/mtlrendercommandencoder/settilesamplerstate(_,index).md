# setTileSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a sampler state to an entry in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setTileSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

```objc
- (void) setTileSamplerState:(id<MTLSamplerState>) sampler atIndex:(NSUInteger) index;
```

#### Discussion

By default, the sampler state at each index is `nil`.

## Parameters

- `sampler`: An [`MTLSamplerState`](../mtlsamplerstate.md) instance the command assigns to an entry in the tile shader argument table for sampler states.
- `index`: An integer that represents the entry in the tile shader argument table for sampler states that stores a record of `sampler`.

## See Also

### Assigning sampler states
- [func setTileSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./settilesamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [func setTileSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./settilesamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the tile shader argument table.
- [func setTileSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./settilesamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstate(_:index:))*