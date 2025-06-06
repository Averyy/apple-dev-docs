# setTileSamplerStates(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple sampler states to a range of entries in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func setTileSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

#### Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setTileSamplerStates:withRange:`](mtlrendercommandencoder/settilesamplerstates:withrange:.md).

 The Objective-C version of this method is [`setTileSamplerStates:withRange:`](mtlrendercommandencoder/settilesamplerstates:withrange:.md).

## Parameters

- `samplers`: An array of   instances the command assigns to entries in the tile shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the tile shader argument table for sampler states. Each entry stores a record of the corresponding element in  .

## See Also

- [func setTileSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/settilesamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the tile shader argument table.
- [func setTileSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/settilesamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [func setTileSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/settilesamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstates(_:range:))*