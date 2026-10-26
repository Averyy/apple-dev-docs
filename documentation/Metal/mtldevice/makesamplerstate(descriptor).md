# makeSamplerState(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a sampler state instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?
```

```objc
- (id<MTLSamplerState>) newSamplerStateWithDescriptor:(MTLSamplerDescriptor *) descriptor;
```

#### Return Value

A new [`MTLSamplerState`](../mtlsamplerstate.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `descriptor`: An [`MTLSamplerDescriptor`](../mtlsamplerdescriptor.md) instance.

## See Also

### Creating samplers
- [func supportsTextureSampleCount(Int) -> Bool](./supportstexturesamplecount%28_%29.md)
  Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [func getDefaultSamplePositions(sampleCount: Int) -> [MTLSamplePosition]](./getdefaultsamplepositions%28samplecount%29.md)
  Returns the default sample locations based on the number of samples.
- [- getDefaultSamplePositions:count:](./getdefaultsamplepositions_count_.md)
  Retrieves the default sample positions for a specific sample count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makesamplerstate(descriptor:))*