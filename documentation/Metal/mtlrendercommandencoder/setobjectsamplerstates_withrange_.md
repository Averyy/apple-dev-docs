# setObjectSamplerStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple sampler states to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObjectSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Swift version of this method is [`setObjectSamplerStates(_:range:)`](./setobjectsamplerstates%28_,range%29.md).

## Parameters

- `samplers`: A pointer to a C array of [`MTLSamplerState`](../mtlsamplerstate.md) instances the command assigns to entries in the object shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the object shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## See Also

### Assigning sampler states for object shaders
- [func setObjectSamplerState((any MTLSamplerState)?, index: Int)](./setobjectsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the object shader argument table.
- [func setObjectSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setobjectsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [- setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./setobjectsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectsamplerstates:withrange:)*