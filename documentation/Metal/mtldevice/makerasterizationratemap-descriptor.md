# makeRasterizationRateMap(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a rasterization rate map instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeRasterizationRateMap(descriptor: MTLRasterizationRateMapDescriptor) -> (any MTLRasterizationRateMap)?
```

#### Return Value

A new [`MTLRasterizationRateMapDescriptor`](mtlrasterizationratemapdescriptor.md) instance if the method completes successfully; otherwise `nil`.

## Parameters

- `descriptor`: An   instance.

## See Also

- [func supportsRasterizationRateMap(layerCount: Int) -> Bool](mtldevice/supportsrasterizationratemap(layercount:).md)
  Returns a Boolean value that indicates whether the GPU can create a rasterization rate map with a specific number of layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerasterizationratemap(descriptor:))*