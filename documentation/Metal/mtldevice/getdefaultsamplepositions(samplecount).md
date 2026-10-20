# getDefaultSamplePositions(sampleCount:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Returns the default sample locations based on the number of samples.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS

## Declaration

```swift
func getDefaultSamplePositions(sampleCount: Int) -> [MTLSamplePosition]
```

#### Return Value

An array of [`MTLSamplePosition`](../mtlsampleposition.md) instances.

#### Discussion

The default sample positions are the same on all GPUs that support programmable sample positions (see [`areProgrammableSamplePositionsSupported`](./areprogrammablesamplepositionssupported.md)).

> **Note**:  GPUs that don’t support programmable sample positions may have different default sample positions that you can’t retrieve.

The default sample position for GPUs that can sample one time is at the pixel’s center.

![Normalized coordinate system diagram that shows a subpixel grid with one point at the center, with coordinates zero-.5, zero-0.5.](https://developer.apple.com/tutorials/images/com.apple.metal/positioning-samples-programmatically-2@2x.png)

The default sample positions for GPUs that can sample two times have locations in the center of the pixel’s second quadrant and fourth quadrants.

![Normalized coordinate system diagram that shows a subpixel grid with two points, one located at zero-.25, zero-0.25. and the other at zero-.75, zero-0.75.](https://developer.apple.com/tutorials/images/com.apple.metal/getDefaultSamplePositions-2@2x.png)

The default sample positions for GPUs that can sample four times have one location in each of the pixel’s quadrants. Each location is at the center of one of that quadrant’s subquadrants.

![Normalized coordinate system diagram that shows a subpixel grid with four points. Each of the pixel’s four quadrants contains one point.](https://developer.apple.com/tutorials/images/com.apple.metal/getDefaultSamplePositions-3@2x.png)

The default sample positions for GPUs that can sample eight times have two locations in each of the pixel’s quadrants.

![Normalized coordinate system diagram that shows a subpixel grid with four points. Each of the pixel’s four quadrants contains two points. ](https://developer.apple.com/tutorials/images/com.apple.metal/getDefaultSamplePositions-4@2x.png)

The table lists the indices and default locations for GPUs that support 1, 2, 4, or 8 sample positions.

| Sample count | Position indices | Subpixel coordinates |
| --- | --- | --- |
| 1 | 0 | (0.5, 0.5) |
| 2 | 0 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 1 | (0.75, 0.75) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.25, 0.25) |
| 4 | 0 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 1 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 2 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 3 | (0.375, 0.125) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.875, 0.375) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.125, 0.625) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.625, 0.875) |
| 8 | 0 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 1 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 2 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 3 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 4 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 5 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 6 ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) 7 | (0.5625, 0.3125) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.4375, 0.6875) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.8125, 0.5625) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.3125, 0.1875) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.1875, 0.8125) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.0625, 0.4375) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.6875, 0.9375) ![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png) (0.9375, 0.0625) |

## Parameters

- `sampleCount`: The number of points a GPU can sample from a texture. Ensure the GPU can support the `sampleCount` value by first calling the device’s [`supportsTextureSampleCount(_:)`](./supportstexturesamplecount%28_%29.md) method.

## See Also

### Creating samplers
- [func supportsTextureSampleCount(Int) -> Bool](./supportstexturesamplecount%28_%29.md)
  Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?](./makesamplerstate%28descriptor%29.md)
  Creates a sampler state instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/getdefaultsamplepositions(samplecount:))*