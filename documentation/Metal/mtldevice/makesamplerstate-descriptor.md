# makeSamplerState(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a sampler state instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?
```

#### Return Value

A new [`MTLSamplerState`](mtlsamplerstate.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `descriptor`: An   instance.

## See Also

- [func supportsTextureSampleCount(Int) -> Bool](mtldevice/supportstexturesamplecount(_:).md)
  Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [func getDefaultSamplePositions(sampleCount: Int) -> [MTLSamplePosition]](mtldevice/getdefaultsamplepositions(samplecount:).md)
  Returns the default sample locations based on the number of samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makesamplerstate(descriptor:))*