# setObjectSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a sampler state to an entry in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setObjectSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

#### Discussion

By default, the sampler state at each index is `nil`.

## Parameters

- `sampler`: An   instance the command assigns to an entry in the object shader argument table for sampler states.
- `index`: An integer that represents the entry in the object argument table for sampler states that stores a record of  .

## See Also

- [func setObjectSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setobjectsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setobjectsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectsamplerstate(_:index:))*