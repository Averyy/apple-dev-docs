# AxisValueLabelCollisionResolution

**Framework**: Swift Charts  
**Kind**: struct

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
struct AxisValueLabelCollisionResolution
```

## Topics

### Type Properties
- [static var automatic: AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution/automatic.md)
  Automatically determine the prevention method based on axis type and data.
- [static var disabled: AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution/disabled.md)
  Do not apply collision resolution to this label. The label will always be displayed.
- [static var greedy: AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution/greedy.md)
  Use a greedy algorithm. Display a label if it’s not overlapping with other labels.
- [static var truncate: AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution/truncate.md)
  Truncate a label to the space available to it.
### Type Methods
- [static func greedy(priority: Double, minimumSpacing: CGFloat?) -> AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution/greedy(priority:minimumspacing:).md)
  Use a greedy algorithm. Display a label if it’s not overlapping with other labels.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [struct AxisValueLabelOrientation](axisvaluelabelorientation.md)
  Describes the orientation of a label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axisvaluelabelcollisionresolution)*