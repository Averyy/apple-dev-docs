# greedy(priority:minimumSpacing:)

**Framework**: Swift Charts  
**Kind**: method

Use a greedy algorithm. Display a label if it’s not overlapping with other labels.

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
static func greedy(priority: Double = 0, minimumSpacing: CGFloat? = nil) -> AxisValueLabelCollisionResolution
```

## Parameters

- `priority`: The priority of the label. A label with higher priority will get placed first by the greedy algorithm.
- `minimumSpacing`: The minimum spacing between the label and its adjacent labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axisvaluelabelcollisionresolution/greedy(priority:minimumspacing:))*