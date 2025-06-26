# RelevantContext.DateKind

**Framework**: RelevanceKit  
**Kind**: struct

Values the system uses as additional context for time-based relevance clues.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct DateKind
```

## Topics

### Date types
- [static var `default`: RelevantContext.DateKind](relevantcontext/datekind/default.md)
  A hint that tells the system to treat a widget with default priority.
- [static var informational: RelevantContext.DateKind](relevantcontext/datekind/informational.md)
  A hint that tells the system to treat a widget with slightly lower priority because it displays content and doesn’t require an action.
- [static var scheduled: RelevantContext.DateKind](relevantcontext/datekind/scheduled.md)
  A hint that tells the system to treat a widget with increased priority because it displays important content or requires action.

## See Also

- [static func date(Date) -> RelevantContext](relevantcontext/date(_:).md)
  Tells the system a widget is relevant at a specific date.
- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(_:kind:).md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(interval:kind:).md)
  Tells the system a widget is relevant for a time interval and provides an additional contextual hint.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(range:kind:).md)
  Tells the system a widget is relevant for a known date range and provides an additional contextual hint.
- [static func date(from: Date, to: Date) -> RelevantContext](relevantcontext/date(from:to:).md)
  Tells the system a widget is relevant between two dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/datekind)*