# AxisMark

**Framework**: Swift Charts  
**Kind**: protocol

A type that serves as the basic building block for the elements of an axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol AxisMark
```

## Mentions

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)

## Topics

### Instance Methods
- [func font(Font?) -> some AxisMark](axismark/font(_:).md)
  Sets the default font for text in this axis content.
- [func foregroundStyle<S>(S) -> some AxisMark](axismark/foregroundstyle(_:).md)
  Sets the axis content’s foreground elements to use a given style.
- [func offset(CGSize) -> some AxisMark](axismark/offset(_:).md)
- [func offset(x: CGFloat, y: CGFloat) -> some AxisMark](axismark/offset(x:y:).md)

## Relationships

### Conforming Types
- [AnyAxisMark](anyaxismark.md)
- [AxisGridLine](axisgridline.md)
- [AxisTick](axistick.md)
- [AxisValueLabel](axisvaluelabel.md)
- [BuilderConditional](builderconditional.md)

## See Also

- [struct AxisTick](axistick.md)
  A mark that a chart draws on an axis to indicate a reference point along that axis.
- [struct AxisGridLine](axisgridline.md)
  A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [struct AxisValueLabel](axisvaluelabel.md)
  A label that describes the value for an axis mark.
- [struct AxisValue](axisvalue.md)
  A value for an axis mark.
- [struct AnyAxisMark](anyaxismark.md)
  A type-erased axis mark.
- [struct AxisMarkBuilder](axismarkbuilder.md)
  A result builder that constructs axis marks and overrides default marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismark)*