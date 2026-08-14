# supportsTextureSampleCount(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func supportsTextureSampleCount(_ sampleCount: Int) -> Bool
```

## Mentions

- [Positioning samples programmatically](positioning-samples-programmatically.md)

#### Discussion

The number of points the GPU can sample a texture varies by device:

| Sample count | Devices |
| --- | --- |
| 1 | All devices |
| 2 | All iOS devices ![None](/images/com.apple.metal/spacer.png) All tvOS devices ![None](/images/com.apple.metal/spacer.png) Some macOS devices |
| 4 | All devices |
| 8 | Some macOS devices |

Consider a GPU device’s limitations for sample count by checking [`MTLTexture`](mtltexture.md)`.`[`sampleCount`](mtltexture/samplecount.md) when configuring these properties:

- [`MTLTextureDescriptor`](mtltexturedescriptor.md)`.`[`sampleCount`](mtltexturedescriptor/samplecount.md)
- [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md)`.`[`rasterSampleCount`](mtlrenderpipelinedescriptor/rastersamplecount.md)
- [`MTLTileRenderPipelineDescriptor`](mtltilerenderpipelinedescriptor.md)`.`[`rasterSampleCount`](mtltilerenderpipelinedescriptor/rastersamplecount.md)
- [`MTLMeshRenderPipelineDescriptor`](mtlmeshrenderpipelinedescriptor.md)`.`[`rasterSampleCount`](mtlmeshrenderpipelinedescriptor/rastersamplecount.md)
- [`MTKView`](https://developer.apple.com/documentation/metalkit/mtkview)`.`[`sampleCount`](https://developer.apple.com/documentation/metalkit/mtkview/samplecount)

## Parameters

- `sampleCount`: The number of points a GPU can sample from a texture.

## See Also

- [func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?](mtldevice/makesamplerstate(descriptor:).md)
  Creates a sampler state instance.
- [func getDefaultSamplePositions(sampleCount: Int) -> [MTLSamplePosition]](mtldevice/getdefaultsamplepositions(samplecount:).md)
  Returns the default sample locations based on the number of samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportstexturesamplecount(_:))*