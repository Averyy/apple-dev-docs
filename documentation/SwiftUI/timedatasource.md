# TimeDataSource

**Framework**: SwiftUI  
**Kind**: struct

A source of time related data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TimeDataSource<Value>
```

#### Overview

Instances of this type provide [`Text`](text.md) with live and automatically updating values in Widgets, Live Activities, watchOS Complications, and of course regular apps.

## Topics

### Type Properties
- [static var currentDate: TimeDataSource<Date>](timedatasource/currentdate.md)
  A time data source that produces `Date.now`.
### Type Methods
- [static func dateRange(endingAt: Date) -> TimeDataSource<Range<Date>>](timedatasource/daterange(endingat:).md)
  A time data source that produces `min(date, Date.now)..<date`.
- [static func dateRange(startingAt: Date) -> TimeDataSource<Range<Date>>](timedatasource/daterange(startingat:).md)
  A time data source that produces `date..<max(date, Date.now)`.
- [static func durationOffset(to: Date) -> TimeDataSource<Duration>](timedatasource/durationoffset(to:).md)
  A time data source that produces the offset between `Date.now` and the given `date` as a `Duration`.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum SystemFormatStyle](systemformatstyle.md)
  A namespace for format styles that implement designs used across Apple’s platformes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timedatasource)*