# setObjectSamplerStates(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple sampler states to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setObjectSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

#### Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setObjectSamplerStates:withRange:`](mtlrendercommandencoder/setobjectsamplerstates:withrange:.md).

## Parameters

- `samplers`: An array of   instances the command assigns to entries in the object shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the object shader argument table for sampler states. Each entry stores a record of the corresponding element in  .

## See Also

- [func setObjectSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the object shader argument table.
- [func setObjectSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setobjectsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectsamplerstates(_:range:))*