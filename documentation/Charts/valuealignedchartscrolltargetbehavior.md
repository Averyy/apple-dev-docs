# ValueAlignedChartScrollTargetBehavior

**Framework**: Swift Charts  
**Kind**: struct

A scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

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
struct ValueAlignedChartScrollTargetBehavior
```

## Topics

### Initializers
- [init(matching: DateComponents, majorAlignment: MajorValueAlignment<Date>?, limitBehavior: ValueAlignedLimitBehavior)](valuealignedchartscrolltargetbehavior/init(matching:majoralignment:limitbehavior:).md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init<T>(unit: T, majorAlignment: MajorValueAlignment<T>?, limitBehavior: ValueAlignedLimitBehavior)](valuealignedchartscrolltargetbehavior/init(unit:majoralignment:limitbehavior:).md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init(xMatching: DateComponents, yMatching: DateComponents, xMajorAlignment: MajorValueAlignment<Date>?, yMajorAlignment: MajorValueAlignment<Date>?, limitBehavior: ValueAlignedLimitBehavior)](valuealignedchartscrolltargetbehavior/init(xmatching:ymatching:xmajoralignment:ymajoralignment:limitbehavior:).md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init<Y>(xMatching: DateComponents, yUnit: Y, xMajorAlignment: MajorValueAlignment<Date>?, yMajorAlignment: MajorValueAlignment<Y>?, limitBehavior: ValueAlignedLimitBehavior)](valuealignedchartscrolltargetbehavior/init(xmatching:yunit:xmajoralignment:ymajoralignment:limitbehavior:).md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init<X>(xUnit: X, yMatching: DateComponents, xMajorAlignment: MajorValueAlignment<X>?, yMajorAlignment: MajorValueAlignment<Date>?, limitBehavior: ValueAlignedLimitBehavior)](valuealignedchartscrolltargetbehavior/init(xunit:ymatching:xmajoralignment:ymajoralignment:limitbehavior:).md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init<X, Y>(xUnit: X, yUnit: Y, xMajorAlignment: MajorValueAlignment<X>?, yMajorAlignment: MajorValueAlignment<Y>?, limitBehavior: ValueAlignedLimitBehavior)](valuealignedchartscrolltargetbehavior/init(xunit:yunit:xmajoralignment:ymajoralignment:limitbehavior:).md)
  Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

## Relationships

### Conforms To
- [ChartScrollTargetBehavior](chartscrolltargetbehavior.md)
- [ScrollTargetBehavior](../SwiftUI/ScrollTargetBehavior.md)

## See Also

- [struct MajorValueAlignment](majorvaluealignment.md)
  A type that defines how the valigned aligned chart scroll target behavior aligns to major values on swipe.
- [struct ValueAlignedLimitBehavior](valuealignedlimitbehavior.md)
  A type that defines the amount of marks that can be scrolled at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/valuealignedchartscrolltargetbehavior)*