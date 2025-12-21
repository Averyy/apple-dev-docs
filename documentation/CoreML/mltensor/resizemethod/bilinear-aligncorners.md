# MLTensor.ResizeMethod.bilinear(alignCorners:)

**Framework**: Core ML  
**Kind**: case

The bilinear interpolation mode where values are computed using bilinear interpolation of 4 neighboring pixels.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case bilinear(alignCorners: Bool = false)
```

#### Discussion

`alignCorners` is a Boolean indicating whether to align the corners of the upscaling grid to the centre of the scaling dimensions rather than the edges.

## See Also

- [MLTensor.ResizeMethod.nearestNeighbor](mltensor/resizemethod/nearestneighbor.md)
  The nearest interpolation mode where values are interpolated using the closest neighbor pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/resizemethod/bilinear(aligncorners:))*