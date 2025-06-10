# date(from:to:)

**Framework**: RelevanceKit  
**Kind**: method

An exact range in time: similar uses as `date()`, but with a known endpoint.

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
static func date(from: Date, to: Date) -> RelevantContext
```

## See Also

- [static func date(Date) -> RelevantContext](relevantcontext/date(_:).md)
  Tells the system a widget is relevant at a specific date.
- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(_:kind:).md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(interval:kind:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint, such as a calendar event.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(range:kind:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint, such as a calendar event.
- [RelevantContext.DateKind](relevantcontext/datekind.md)
  Values the system uses as additional context for time-based relevance clues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(from:to:))*