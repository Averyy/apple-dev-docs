# MajorValueAlignment

**Framework**: Swift Charts  
**Kind**: struct

A type that defines how the valigned aligned chart scroll target behavior aligns to major values on swipe.

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
struct MajorValueAlignment<Value> where Value : Plottable
```

## Topics

### Type Properties
- [static var page: MajorValueAlignment<Value>](majorvaluealignment/page.md)
  Automatically set the major aligment unit to be the size of the visible domain which is equivalent to a page.
### Type Methods
- [static func matching(DateComponents) -> MajorValueAlignment<Value>](majorvaluealignment/matching(_:).md)
  Align to calendar components.
- [static func unit(Value) -> MajorValueAlignment<Value>](majorvaluealignment/unit(_:).md)
  Align to units.

## See Also

- [struct ValueAlignedLimitBehavior](valuealignedlimitbehavior.md)
  A type that defines the amount of marks that can be scrolled at a time.
- [struct ValueAlignedChartScrollTargetBehavior](valuealignedchartscrolltargetbehavior.md)
  A scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/majorvaluealignment)*