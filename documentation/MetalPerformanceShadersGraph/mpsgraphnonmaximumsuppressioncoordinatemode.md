# MPSGraphNonMaximumSuppressionCoordinateMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The non-maximum suppression coordinate mode.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphNonMaximumSuppressionCoordinateMode
```

#### Overview

The coordinate mode to use. At initialization defaults to MPSGraphNonMaximumSuppressionCoordinateModeCornersHeightFirst. This mode specifies the representation used for the 4 box coordinate values. Center coordinate modes define a centered box and the box dimensions.

```md
CornersHeightFirst:
    [h_start, w_start, h_end, w_end]
CornersWidthFirst:
    [w_start, h_start, w_end, h_end]
CentersHeightFirst:
    [h_center, w_center, box_height, box_width]
CentersWidthFirst:
    [w_center, w_center, box_height, box_width]
```

## Topics

### Enumeration Cases
- [MPSGraphNonMaximumSuppressionCoordinateMode.centersHeightFirst](mpsgraphnonmaximumsuppressioncoordinatemode/centersheightfirst.md)
- [MPSGraphNonMaximumSuppressionCoordinateMode.centersWidthFirst](mpsgraphnonmaximumsuppressioncoordinatemode/centerswidthfirst.md)
- [MPSGraphNonMaximumSuppressionCoordinateMode.cornersWidthFirst](mpsgraphnonmaximumsuppressioncoordinatemode/cornerswidthfirst.md)
- [MPSGraphNonMaximumSuppressionCoordinateMode.explicit](mpsgraphnonmaximumsuppressioncoordinatemode/explicit.md)
### Initializers
- [init?(rawValue: UInt)](mpsgraphnonmaximumsuppressioncoordinatemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphnonmaximumsuppressioncoordinatemode)*