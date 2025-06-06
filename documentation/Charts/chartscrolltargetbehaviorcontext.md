# ChartScrollTargetBehaviorContext

**Framework**: Swift Charts  
**Kind**: struct

Contextual information that you can use to determine how to best adjust how charts scroll.

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
@dynamicMemberLookup
struct ChartScrollTargetBehaviorContext
```

## Topics

### Instance Properties
- [var chartProxy: ChartProxy](chartscrolltargetbehaviorcontext/chartproxy.md)
  The chart proxy that you use to access the scales and plot area of the chart.
### Subscripts
- [subscript<T>(dynamicMember _: KeyPath<ScrollTargetBehaviorContext, T>) -> T](chartscrolltargetbehaviorcontext/subscript(dynamicmember:).md)

## See Also

- [protocol ChartScrollTargetBehavior](chartscrolltargetbehavior.md)
  A type that configures the scroll behavior of charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartscrolltargetbehaviorcontext)*