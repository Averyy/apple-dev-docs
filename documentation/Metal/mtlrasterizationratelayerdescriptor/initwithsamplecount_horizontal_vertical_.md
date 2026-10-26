# initWithSampleCount:horizontal:vertical:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Initializes the layer map with the provided grid size and rasterization rates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithSampleCount:(MTLSize) sampleCount horizontal:(const float *) horizontal vertical:(const float *) vertical;
```

#### Return Value

A layer descriptor with a grid of the specified size. The layer descriptor copies the  rasterization rates.

## Parameters

- `sampleCount`: The size of the grid. Specify the width and height to determine the number of columns and rows in the layer map. The initializer ignores the depth component.
- `horizontal`: The rasterization rates for the layer map’s columns. There needs to be at least as many samples as the width you specified in `sampleCount`.
- `vertical`: The rasterization rates for the layer map’s columns. There needs to be at least as many samples as the height you specified in `sampleCount`.

## See Also

### Creating a layer rasterization rate descriptor
- [init(sampleCount: MTLSize)](./init%28samplecount%29.md)
  Initializes the layer map with an empty grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/initwithsamplecount:horizontal:vertical:)*