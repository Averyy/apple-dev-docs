# setTileSamplerStates(_:lodMinClamps:lodMaxClamps:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func setTileSamplerStates(_ samplers: [(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)
```

#### Discussion

Each element of the method’s `lodMinClamps` and `lodMaxClamps` parameters overrides the default values for the corresponding sampler in `samplers`. You can set a sampler’s default values by configuring the [`lodMinClamp`](mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](mtlsamplerdescriptor/lodmaxclamp.md) properties of [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:`](mtlrendercommandencoder/settilesamplerstates:lodminclamps:lodmaxclamps:withrange:.md).

 The Objective-C version of this method is [`setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:`](mtlrendercommandencoder/settilesamplerstates:lodminclamps:lodmaxclamps:withrange:.md).

## Parameters

- `samplers`: An array of   instances the command assigns to entries in the tile shader argument table for sampler states.
- `lodMinClamps`: An array of floating-point values. Each element is the smallest level of detail value a tile shader can use when it samples a texture with the corresponding element in  .
- `lodMaxClamps`: An array of floating-point values. Each element is the largest level of detail value a tile shader can use when it samples a texture with the corresponding element in  .
- `range`: A span of integers that represent the entries in the tile shader argument table for sampler states. Each entry stores a record of the corresponding element in  .

## See Also

- [func setTileSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/settilesamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the tile shader argument table.
- [func setTileSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/settilesamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [func setTileSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/settilesamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstates(_:lodminclamps:lodmaxclamps:range:))*