# AXChartDescriptor.ContentDirection

**Framework**: Accessibility  
**Kind**: enum  
**Role**: Enumeration

A constant that describes the content direction of the chart.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum ContentDirection
```

```c
enum AXChartDescriptorContentDirection : NSInteger;
```

#### Overview

Use content direction to specify the direction of the x-axis, which the audio graph represents as time. For example, a bar chart might have a content direction of [`AXChartDescriptor.ContentDirection.leftToRight`](./contentdirection-swift.enum/lefttoright.md), and a pie chart might have a content direction of [`AXChartDescriptor.ContentDirection.radialClockwise`](./contentdirection-swift.enum/radialclockwise.md).

## Topics

### Content directions
- [AXChartDescriptor.ContentDirection.leftToRight](./contentdirection-swift.enum/lefttoright.md)
  A content direction with an x-axis that increases from left to right.
- [AXChartDescriptor.ContentDirection.rightToLeft](./contentdirection-swift.enum/righttoleft.md)
  A content direction with an x-axis that increases from right to left.
- [AXChartDescriptor.ContentDirection.bottomToTop](./contentdirection-swift.enum/bottomtotop.md)
  A content direction with an x-axis that increases from bottom to top.
- [AXChartDescriptor.ContentDirection.topToBottom](./contentdirection-swift.enum/toptobottom.md)
  A content direction with an x-axis that increases from top to bottom.
- [AXChartDescriptor.ContentDirection.radialClockwise](./contentdirection-swift.enum/radialclockwise.md)
  A content direction with a radial x-axis that increases clockwise.
- [AXChartDescriptor.ContentDirection.radialCounterClockwise](./contentdirection-swift.enum/radialcounterclockwise.md)
  A content direction with a radial x-axis that increases counterclockwise.
### Initializers
- [init?(rawValue: Int)](./contentdirection-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the content layout
- [var contentFrame: CGRect](./contentframe.md)
  The bounds of the view, in screen coordinates, for visually rendering data values.
- [var contentDirection: AXChartDescriptor.ContentDirection](./contentdirection-swift.property.md)
  The direction of the content in the chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axchartdescriptor/contentdirection-swift.enum)*