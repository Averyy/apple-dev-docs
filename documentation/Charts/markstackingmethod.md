# MarkStackingMethod

**Framework**: Swift Charts  
**Kind**: struct

The ways in which you can stack marks in a chart.

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
@frozen
struct MarkStackingMethod
```

## Topics

### Type Properties
- [static var center: MarkStackingMethod](markstackingmethod/center.md)
  Stack marks using a center offset.
- [static var normalized: MarkStackingMethod](markstackingmethod/normalized.md)
  Create normalized stacked bar and area charts.
- [static var standard: MarkStackingMethod](markstackingmethod/standard.md)
  Stack marks starting at zero.
- [static var unstacked: MarkStackingMethod](markstackingmethod/unstacked.md)
  Don’t stack marks.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MarkDimension](markdimension.md)
  An individual dimension representing a mark’s width or height.
- [struct InterpolationMethod](interpolationmethod.md)
  The ways in which line or area marks interpolate their data.
- [struct BasicChartSymbolShape](basicchartsymbolshape.md)
  A basic chart symbol shape.
- [protocol ChartSymbolShape](chartsymbolshape.md)
  A type that can act as a shape for the marks that you add to a chart.
- [struct AnyChartSymbolShape](anychartsymbolshape.md)
  A type-erased plotting shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/markstackingmethod)*