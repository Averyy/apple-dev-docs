# AxisMarkValues

**Framework**: Swift Charts  
**Kind**: struct

Describes the values the axis markers will present (one for each value).

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
struct AxisMarkValues
```

## Topics

### Type Properties
- [static var automatic: AxisMarkValues](axismarkvalues/automatic.md)
  Automatically determines the values for the markers of the axis.
### Type Methods
- [static func automatic(desiredCount: Int?, roundLowerBound: Bool?, roundUpperBound: Bool?) -> AxisMarkValues](axismarkvalues/automatic(desiredcount:roundlowerbound:roundupperbound:).md)
  Automatically determines the values for the markers, approximating the target number of values.
- [static func automatic<P>(minimumStride: P, desiredCount: Int?, roundLowerBound: Bool?, roundUpperBound: Bool?) -> AxisMarkValues](axismarkvalues/automatic(minimumstride:desiredcount:roundlowerbound:roundupperbound:).md)
- [static func stride(by: Calendar.Component, count: Int, roundLowerBound: Bool?, roundUpperBound: Bool?, calendar: Calendar?) -> AxisMarkValues](axismarkvalues/stride(by:count:roundlowerbound:roundupperbound:calendar:).md)
  Creates values with the given calendar unit.
- [static func stride<P>(by: P, roundLowerBound: Bool?, roundUpperBound: Bool?) -> AxisMarkValues](axismarkvalues/stride(by:roundlowerbound:roundupperbound:).md)
  Creates values with the given number step.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [struct AxisMarkPreset](axismarkpreset.md)
  Describes preset styles for axis markers.
- [struct AxisMarkPosition](axismarkposition.md)
  Describes the position of axis markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismarkvalues)*