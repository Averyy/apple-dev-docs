# setObjectSamplerStates(_:lodMinClamps:lodMaxClamps:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setObjectSamplerStates(_ samplers: [(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)
```

#### Discussion

Each element of the method’s `lodMinClamps` and `lodMaxClamps` parameters overrides the default values for the corresponding sampler in `samplers`. You can set a sampler’s default values by configuring the [`lodMinClamp`](mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](mtlsamplerdescriptor/lodmaxclamp.md) properties of [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:`](mtlrendercommandencoder/setobjectsamplerstates:lodminclamps:lodmaxclamps:withrange:.md).

## Parameters

- `samplers`: An array of   instances the command assigns to entries in the object shader argument table for sampler states.
- `lodMinClamps`: An array of floating-point values. Each element is the smallest level of detail value an object shader can use when it samples a texture with the corresponding element in  .
- `lodMaxClamps`: An array of floating-point values. Each element is the largest level of detail value an object shader can use when it samples a texture with the corresponding element in  .
- `range`: A span of integers that represent the entries in the object shader argument table for sampler states. Each entry stores a record of the corresponding element in  .

## See Also

- [func setObjectSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the object shader argument table.
- [func setObjectSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setobjectsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectsamplerstates(_:lodminclamps:lodmaxclamps:range:))*