# init(unit:majorAlignment:limitBehavior:)

**Framework**: Swift Charts  
**Kind**: init

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
nonisolated
init<T>(unit: T, majorAlignment: MajorValueAlignment<T>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic) where T : Plottable, T : Numeric
```

## Parameters

- `unit`: The alignment unit. When the user finishes a scroll gesture, the chart will snap to align to   the given unit or the end of the domain.
- `majorAlignment`: The behavior for aligning to major values. When the user swipes on the chart, the chart will snap to the   next or previous major unit depending on the swipe direction. When enabled, the default major unit is a page.
- `limitBehavior`: The scroll limit behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/valuealignedchartscrolltargetbehavior/init(unit:majoralignment:limitbehavior:))*