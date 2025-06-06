# setMeshSamplerState(_:lodMinClamp:lodMaxClamp:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a sampler state and clamp values to an entry in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setMeshSamplerState(_ sampler: (any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)
```

#### Discussion

The method’s `lodMinClamp` and `lodMaxClamp` parameters override the default values for `sampler`. You can set the sampler’s default values by configuring the [`lodMinClamp`](mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](mtlsamplerdescriptor/lodmaxclamp.md) properties of [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

## Parameters

- `sampler`: An   instance the command assigns to an entry in the mesh shader argument table for sampler states.
- `lodMinClamp`: The smallest level of detail value a mesh shader can use when it samples a texture.
- `lodMaxClamp`: The largest level of detail value a mesh shader can use when it samples a texture.
- `index`: An integer that represents the entry in the mesh shader argument table for sampler states that stores a record of  .

## See Also

- [func setMeshSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setmeshsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the mesh shader argument table.
- [func setMeshSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setmeshsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the mesh shader argument table.
- [func setMeshSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setmeshsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshsamplerstate(_:lodminclamp:lodmaxclamp:index:))*