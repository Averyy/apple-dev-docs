# generatesCalendarDates

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/swift/true) if the formatter generates the deprecated [`NSCalendarDate`](nscalendardate.md) type, and is [`false`](https://developer.apple.com/documentation/swift/false) otherwise. You should use [`Date`](date.md) and [`Calendar`](calendar.md) rather than [`NSCalendarDate`](nscalendardate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/generatescalendardates)*