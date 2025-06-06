# getDefaultSamplePositions(sampleCount:)

**Framework**: Metal  
**Kind**: method

Returns the default sample locations based on the number of samples.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func getDefaultSamplePositions(sampleCount: Int) -> [MTLSamplePosition]
```

#### Return Value

An array of [`MTLSamplePosition`](mtlsampleposition.md) instances.

#### Discussion

The default sample positions are the same on all GPUs that support programmable sample positions (see [`areProgrammableSamplePositionsSupported`](mtldevice/areprogrammablesamplepositionssupported.md)).

> **Note**:  GPUs that don’t support programmable sample positions may have different default sample positions that you can’t retrieve.

 GPUs that don’t support programmable sample positions may have different default sample positions that you can’t retrieve.

The default sample position for GPUs that can sample one time is at the pixel’s center.

![Normalized coordinate system diagram that shows a subpixel grid with one point at the center, with coordinates zero-.5, zero-0.5.](https://docs-assets.developer.apple.com/published/b82e8ada6eb98fc644df94e8d27c8eb1/media-4062028%402x.png)

The default sample positions for GPUs that can sample two times have locations in the center of the pixel’s second quadrant and fourth quadrants.

![Normalized coordinate system diagram that shows a subpixel grid with two points, one located at zero-.25, zero-0.25. and the other at zero-.75, zero-0.75.](https://docs-assets.developer.apple.com/published/0326b2b19119cd5568f173d4087b10c4/media-4062030%402x.png)

The default sample positions for GPUs that can sample four times have one location in each of the pixel’s quadrants. Each location is at the center of one of that quadrant’s subquadrants.

![Normalized coordinate system diagram that shows a subpixel grid with four points. Each of the pixel’s four quadrants contains one point.](https://docs-assets.developer.apple.com/published/75241ff22d0b2ee42446c2860eca985d/media-4062036%402x.png)

The default sample positions for GPUs that can sample eight times have two locations in each of the pixel’s quadrants.

![Normalized coordinate system diagram that shows a subpixel grid with four points. Each of the pixel’s four quadrants contains two points. ](https://docs-assets.developer.apple.com/published/b0987ba0ce96b5853f689931e9496f22/media-4062024%402x.png)

The table lists the indices and default locations for GPUs that support one, two, four, or eight sample positions.

| Sample count | Position indices | Subpixel coordinates |
| --- | --- | --- |
| 1 | 0 | (0.5, 0.5) |
| 2 | 0 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 | (0.75, 0.75) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.25, 0.25) |
| 4 | 0 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 2 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 3 | (0.375, 0.125) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.875, 0.375) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.125, 0.625) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.625, 0.875) |
| 8 | 0 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 2 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 3 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 4 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 5 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 6 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 7 | (0.5625, 0.3125) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.4375, 0.6875) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.8125, 0.5625) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.3125, 0.1875) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.1875, 0.8125) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.0625, 0.4375) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.6875, 0.9375) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.9375, 0.0625) |

## Parameters

- `sampleCount`: The number of points a GPU can sample from a texture. Ensure the GPU can support the   value by first calling the device’s   method.

## See Also

- [func supportsTextureSampleCount(Int) -> Bool](mtldevice/supportstexturesamplecount(_:).md)
  Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?](mtldevice/makesamplerstate(descriptor:).md)
  Creates a sampler state instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/getdefaultsamplepositions(samplecount:))*