# generatesCalendarDates

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the formatter generates the deprecated calendar date type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var generatesCalendarDates: Bool { get set }
```

```objc
@property BOOL generatesCalendarDates;
```

#### Discussion

This property is [`true`](../../Swift/true.md) if the formatter generates the deprecated [`NSCalendarDate`](../nscalendardate.md) type, and is [`false`](../../Swift/false.md) otherwise. You should use [`Date`](../date.md) and [`Calendar`](../calendar.md) rather than [`NSCalendarDate`](../nscalendardate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/generatescalendardates)*