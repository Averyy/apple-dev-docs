# setSamplerStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes multiple texture samplers, allowing compute kernels to use them for sampling textures on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Discussion

> ⚠️ **Warning**:  This method requires that the number of instances in `samplers` be the same as the length of `range`.

## Parameters

- `samplers`: An array of [`MTLSamplerState`](../mtlsamplerstate.md) instances to bind to the sampler argument table.
- `range`: The sampler table indexes to bind each of the `samplers` to, in the order they appear.

## See Also

### Binding texture samplers
- [func setSamplerState((any MTLSamplerState)?, index: Int)](./setsamplerstate%28_,index%29.md)
  Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [- setSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./setsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Encodes multiple texture samplers with custom levels of detail clamping, allowing compute kernels to use them for sampling textures on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstates:withrange:)*