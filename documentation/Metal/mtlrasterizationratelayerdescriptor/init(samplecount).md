# init(sampleCount:)

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Initializes the layer map with an empty grid.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(sampleCount: MTLSize)
```

```objc
- (instancetype) initWithSampleCount:(MTLSize) sampleCount;
```

#### Return Value

A layer descriptor with a grid of the specified size. All of the rasterization rates are set to `0.0`.

## Parameters

- `sampleCount`: The size of the grid. Specify the width and height to determine the number of columns and rows in the layer map. The initializer ignores the depth component.

## See Also

### Creating a layer rasterization rate descriptor
- [convenience init(horizontal: [Float], vertical: [Float])](./init%28horizontal,vertical%29.md)
  Initializes a layer rate map with a set of horizontal and vertical rasterization rates.
- [- initWithSampleCount:horizontal:vertical:](./initwithsamplecount_horizontal_vertical_.md)
  Initializes the layer map with the provided grid size and rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/init(samplecount:))*