# supportsRasterizationRateMap(layerCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the GPU can create a rasterization rate map with a specific number of layers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func supportsRasterizationRateMap(layerCount: Int) -> Bool
```

## Parameters

- `layerCount`: The number of layers for a rasterization rate map.

## See Also

- [func makeRasterizationRateMap(descriptor: MTLRasterizationRateMapDescriptor) -> (any MTLRasterizationRateMap)?](mtldevice/makerasterizationratemap(descriptor:).md)
  Creates a rasterization rate map instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsrasterizationratemap(layercount:))*