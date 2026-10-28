# setMeshSamplerStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple sampler states to a range of entries in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setMeshSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Discussion

By default, the sampler state at each index is `nil`.

> **Note**:  The Swift version of this method is [`setMeshSamplerStates(_:range:)`](./setmeshsamplerstates%28_,range%29.md).

## Parameters

- `samplers`: A pointer to a C array of [`MTLSamplerState`](../mtlsamplerstate.md) instances the command assigns to entries in the mesh shader argument table for sampler states.
- `range`: A span of integers that represent the entries in the mesh shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## See Also

### Assigning sampler states for mesh shaders
- [func setMeshSamplerState((any MTLSamplerState)?, index: Int)](./setmeshsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the mesh shader argument table.
- [func setMeshSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./setmeshsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [- setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./setmeshsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates:withrange:)*