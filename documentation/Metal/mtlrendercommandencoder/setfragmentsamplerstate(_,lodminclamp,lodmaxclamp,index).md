# setFragmentSamplerState(_:lodMinClamp:lodMaxClamp:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a sampler state and clamp values to an entry in the fragment shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setFragmentSamplerState(_ sampler: (any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)
```

```objc
- (void) setFragmentSamplerState:(id<MTLSamplerState>) sampler lodMinClamp:(float) lodMinClamp lodMaxClamp:(float) lodMaxClamp atIndex:(NSUInteger) index;
```

#### Discussion

The method’s `lodMinClamp` and `lodMaxClamp` parameters override the default values for `sampler`. You can set the sampler’s default values by configuring the [`lodMinClamp`](../mtlsamplerdescriptor/lodminclamp.md) and [`lodMaxClamp`](../mtlsamplerdescriptor/lodmaxclamp.md) properties of [`MTLSamplerDescriptor`](../mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

## Parameters

- `sampler`: An [`MTLSamplerState`](../mtlsamplerstate.md) instance the command assigns to an entry in the fragment shader argument table for sampler states.
- `lodMinClamp`: The smallest level of detail value a fragment shader can use when it samples a texture.
- `lodMaxClamp`: The largest level of detail value a fragment shader can use when it samples a texture.
- `index`: An integer that represents the entry in the fragment shader argument table for sampler states that stores a record of `sampler`.

## See Also

### Assigning sampler states
- [func setFragmentSamplerState((any MTLSamplerState)?, index: Int)](./setfragmentsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the fragment shader argument table.
- [func setFragmentSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./setfragmentsamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [func setFragmentSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./setfragmentsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate(_:lodminclamp:lodmaxclamp:index:))*