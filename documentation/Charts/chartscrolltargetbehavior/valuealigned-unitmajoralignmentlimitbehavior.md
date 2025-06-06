# valueAligned(unit:majorAlignment:limitBehavior:)

**Framework**: Swift Charts  
**Kind**: method

Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func valueAligned<P>(unit: P, majorAlignment: MajorValueAlignment<P>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic) -> ValueAlignedChartScrollTargetBehavior where Self == ValueAlignedChartScrollTargetBehavior, P : Plottable, P : Numeric
```

#### Discussion

Use this method to create a scroll behavior that aligns to desired units.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.horizontal)
.chartScrollTargetBehavior(.valueAligned(unit: 10))
```

The value aligned behavior can be set to align to major units on swipes. When enabled, the default major unit is a page and the behavior on swipe is similar to the `.paged` behavior.

## Parameters

- `unit`: The alignment unit. When the user finishes a scroll gesture, the chart will snap to align to   the given unit or the end of the domain.
- `majorAlignment`: The behavior for aligning to major values. When the user swipes on the chart, the chart will snap to the   next or previous major unit depending on the swipe direction. When enabled, the default major unit is a page.
- `limitBehavior`: The scroll limit behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartscrolltargetbehavior/valuealigned(unit:majoralignment:limitbehavior:))*