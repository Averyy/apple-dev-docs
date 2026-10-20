# AxisMarkValues

**Framework**: Swift Charts  
**Kind**: struct  
**Role**: Structure

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
- [static var automatic: AxisMarkValues](./axismarkvalues/automatic.md)
  Automatically determines the values for the markers of the axis.
### Type Methods
- [static func automatic(desiredCount: Int?, roundLowerBound: Bool?, roundUpperBound: Bool?) -> AxisMarkValues](./axismarkvalues/automatic%28desiredcount,roundlowerbound,roundupperbound%29.md)
  Automatically determines the values for the markers, approximating the target number of values.
- [static func automatic<P>(minimumStride: P, desiredCount: Int?, roundLowerBound: Bool?, roundUpperBound: Bool?) -> AxisMarkValues](./axismarkvalues/automatic%28minimumstride,desiredcount,roundlowerbound,roundupperbound%29.md)
- [static func stride(by: Calendar.Component, count: Int, roundLowerBound: Bool?, roundUpperBound: Bool?, calendar: Calendar?) -> AxisMarkValues](./axismarkvalues/stride%28by,count,roundlowerbound,roundupperbound,calendar%29.md)
  Creates values with the given calendar unit.
- [static func stride<P>(by: P, roundLowerBound: Bool?, roundUpperBound: Bool?) -> AxisMarkValues](./axismarkvalues/stride%28by,roundlowerbound,roundupperbound%29.md)
  Creates values with the given number step.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)

## See Also

### Supporting types
- [struct AxisMarkPreset](./axismarkpreset.md)
  Describes preset styles for axis markers.
- [struct AxisMarkPosition](./axismarkposition.md)
  Describes the position of axis markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismarkvalues)*