# RelevantContext.DateKind

**Framework**: RelevanceKit  
**Kind**: struct  
**Role**: Structure

Values the system uses as additional context for time-based relevance clues.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct DateKind
```

## Topics

### Date types
- [static var `default`: RelevantContext.DateKind](./datekind/default.md)
  A hint that tells the system to treat a widget with default priority.
- [static var informational: RelevantContext.DateKind](./datekind/informational.md)
  A hint that tells the system to treat a widget with slightly lower priority because it displays content and doesn’t require an action.
- [static var scheduled: RelevantContext.DateKind](./datekind/scheduled.md)
  A hint that tells the system to treat a widget with increased priority because it displays important content or requires action.

## See Also

### Time clues
- [static func date(Date) -> RelevantContext](./date%28_%29.md)
  Tells the system a widget is relevant at a specific date.
- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](./date%28_,kind%29.md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext](./date%28interval,kind%29.md)
  Tells the system a widget is relevant for a time interval and provides an additional contextual hint.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](./date%28range,kind%29.md)
  Tells the system a widget is relevant for a known date range and provides an additional contextual hint.
- [static func date(from: Date, to: Date) -> RelevantContext](./date%28from,to%29.md)
  Tells the system a widget is relevant between two dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/datekind)*