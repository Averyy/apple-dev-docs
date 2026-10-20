# ChartScrollTargetBehavior

**Framework**: Swift Charts  
**Kind**: protocol  
**Role**: Protocol

A type that configures the scroll behavior of charts.

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
protocol ChartScrollTargetBehavior : ScrollTargetBehavior
```

## Topics

### Supporting types
- [struct MajorValueAlignment](./majorvaluealignment.md)
  A type that defines how the valigned aligned chart scroll target behavior aligns to major values on swipe.
- [struct ValueAlignedLimitBehavior](./valuealignedlimitbehavior.md)
  A type that defines the amount of marks that can be scrolled at a time.
- [struct ValueAlignedChartScrollTargetBehavior](./valuealignedchartscrolltargetbehavior.md)
  A scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
### Instance Methods
- [func updateTarget(inout ScrollTarget, context: ChartScrollTargetBehaviorContext)](./chartscrolltargetbehavior/updatetarget%28_,context%29.md)
### Type Methods
- [static func valueAligned(matching: DateComponents, majorAlignment: MajorValueAlignment<Date>?, limitBehavior: ValueAlignedLimitBehavior) -> ValueAlignedChartScrollTargetBehavior](./chartscrolltargetbehavior/valuealigned%28matching,majoralignment,limitbehavior%29.md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [static func valueAligned<P>(unit: P, majorAlignment: MajorValueAlignment<P>?, limitBehavior: ValueAlignedLimitBehavior) -> ValueAlignedChartScrollTargetBehavior](./chartscrolltargetbehavior/valuealigned%28unit,majoralignment,limitbehavior%29.md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [static func valueAligned(xMatching: DateComponents, yMatching: DateComponents, xMajorAlignment: MajorValueAlignment<Date>?, yMajorAlignment: MajorValueAlignment<Date>?, limitBehavior: ValueAlignedLimitBehavior) -> ValueAlignedChartScrollTargetBehavior](./chartscrolltargetbehavior/valuealigned%28xmatching,ymatching,xmajoralignment,ymajoralignment,limitbehavior%29.md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [static func valueAligned<Y>(xMatching: DateComponents, yUnit: Y, xMajorAlignment: MajorValueAlignment<Date>?, yMajorAlignment: MajorValueAlignment<Y>?, limitBehavior: ValueAlignedLimitBehavior) -> ValueAlignedChartScrollTargetBehavior](./chartscrolltargetbehavior/valuealigned%28xmatching,yunit,xmajoralignment,ymajoralignment,limitbehavior%29.md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [static func valueAligned<X>(xUnit: X, yMatching: DateComponents, xMajorAlignment: MajorValueAlignment<X>?, yMajorAlignment: MajorValueAlignment<Date>?, limitBehavior: ValueAlignedLimitBehavior) -> ValueAlignedChartScrollTargetBehavior](./chartscrolltargetbehavior/valuealigned%28xunit,ymatching,xmajoralignment,ymajoralignment,limitbehavior%29.md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [static func valueAligned<X, Y>(xUnit: X, yUnit: Y, xMajorAlignment: MajorValueAlignment<X>?, yMajorAlignment: MajorValueAlignment<Y>?, limitBehavior: ValueAlignedLimitBehavior) -> ValueAlignedChartScrollTargetBehavior](./chartscrolltargetbehavior/valuealigned%28xunit,yunit,xmajoralignment,ymajoralignment,limitbehavior%29.md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
### Default Implementations
- [ScrollTargetBehavior Implementations](./chartscrolltargetbehavior/scrolltargetbehavior-implementations.md)

## Relationships

### Inherits From
- [ScrollTargetBehavior](../SwiftUI/scrolltargetbehavior.md)
### Conforming Types
- [ValueAlignedChartScrollTargetBehavior](./valuealignedchartscrolltargetbehavior.md)

## See Also

### Scrolling
- [struct ChartScrollTargetBehaviorContext](./chartscrolltargetbehaviorcontext.md)
  Contextual information that you can use to determine how to best adjust how charts scroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartscrolltargetbehavior)*