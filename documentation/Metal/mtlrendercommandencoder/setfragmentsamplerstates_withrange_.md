# setFragmentSamplerStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple sampler states to a range of entries in the fragment shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setFragmentSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Swift version of this method is [`setFragmentSamplerStates(_:range:)`](./setfragmentsamplerstates%28_,range%29.md).

## Parameters

- `samplers`: A pointer to a C array of [`MTLSamplerState`](../mtlsamplerstate.md) instances the command assigns to entries in the fragment shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the fragment shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## See Also

### Assigning sampler states
- [func setFragmentSamplerState((any MTLSamplerState)?, index: Int)](./setfragmentsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the fragment shader argument table.
- [func setFragmentSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setfragmentsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [- setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./setfragmentsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates:withrange:)*