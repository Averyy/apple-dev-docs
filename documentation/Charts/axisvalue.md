# AxisValue

**Framework**: Swift Charts  
**Kind**: struct

A value for an axis mark.

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
struct AxisValue
```

## Topics

### Instance Properties
- [var count: Int](axisvalue/count.md)
  The number of values on this axis.
- [var index: Int](axisvalue/index.md)
  The index of the value along the axis.
### Instance Methods
- [func `as`<P>(P.Type) -> P?](axisvalue/as(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol AxisMark](axismark.md)
  A type that serves as the basic building block for the elements of an axis.
- [struct AxisTick](axistick.md)
  A mark that a chart draws on an axis to indicate a reference point along that axis.
- [struct AxisGridLine](axisgridline.md)
  A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [struct AxisValueLabel](axisvaluelabel.md)
  A label that describes the value for an axis mark.
- [struct AnyAxisMark](anyaxismark.md)
  A type-erased axis mark.
- [struct AxisMarkBuilder](axismarkbuilder.md)
  A result builder that constructs axis marks and overrides default marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axisvalue)*