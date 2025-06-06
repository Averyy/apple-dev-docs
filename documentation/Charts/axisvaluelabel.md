# AxisValueLabel

**Framework**: Swift Charts  
**Kind**: struct

A label that describes the value for an axis mark.

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
struct AxisValueLabel<Content> where Content : View
```

## Mentions

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)

## Topics

### Supporting types
- [struct AxisValueLabelOrientation](axisvaluelabelorientation.md)
  Describes the orientation of a label.
- [struct AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution.md)
### Initializers
- [init(LocalizedStringKey, centered: Bool?, anchor: UnitPoint?, multiLabelAlignment: Alignment?, collisionResolution: AxisValueLabelCollisionResolution, offsetsMarks: Bool?, orientation: AxisValueLabelOrientation, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?)](axisvaluelabel/init(_:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:)-9202h.md)
  Constructs an axis value label with the given properties to display the given string.
- [init<S>(S, centered: Bool?, anchor: UnitPoint?, multiLabelAlignment: Alignment?, collisionResolution: AxisValueLabelCollisionResolution, offsetsMarks: Bool?, orientation: AxisValueLabelOrientation, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?)](axisvaluelabel/init(_:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:)-9rytf.md)
  Constructs an axis value label with the given properties to display the given string.
- [init(centered: Bool?, anchor: UnitPoint?, multiLabelAlignment: Alignment?, collisionResolution: AxisValueLabelCollisionResolution, offsetsMarks: Bool?, orientation: AxisValueLabelOrientation, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?)](axisvaluelabel/init(centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:).md)
  Constructs axis value labels with the given properties and default text.
- [init(centered: Bool?, anchor: UnitPoint?, multiLabelAlignment: Alignment?, collisionResolution: AxisValueLabelCollisionResolution, offsetsMarks: Bool?, orientation: AxisValueLabelOrientation, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?, content: () -> Content)](axisvaluelabel/init(centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:content:).md)
  Constructs an axis value label with the given properties to display the given content.
- [init<Format>(format: Format, centered: Bool?, anchor: UnitPoint?, multiLabelAlignment: Alignment?, collisionResolution: AxisValueLabelCollisionResolution, offsetsMarks: Bool?, orientation: AxisValueLabelOrientation, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?)](axisvaluelabel/init(format:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:).md)
  Constructs an axis value label with the given properties to display the given content.

## Relationships

### Conforms To
- [AxisMark](axismark.md)

## See Also

- [protocol AxisMark](axismark.md)
  A type that serves as the basic building block for the elements of an axis.
- [struct AxisTick](axistick.md)
  A mark that a chart draws on an axis to indicate a reference point along that axis.
- [struct AxisGridLine](axisgridline.md)
  A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [struct AxisValue](axisvalue.md)
  A value for an axis mark.
- [struct AnyAxisMark](anyaxismark.md)
  A type-erased axis mark.
- [struct AxisMarkBuilder](axismarkbuilder.md)
  A result builder that constructs axis marks and overrides default marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axisvaluelabel)*