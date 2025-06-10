# date(interval:kind:)

**Framework**: RelevanceKit  
**Kind**: method

An exact range in time: similar uses as `date()`, but with a known endpoint, such as a calendar event.

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
static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext
```

## See Also

- [static func date(Date) -> RelevantContext](relevantcontext/date(_:).md)
  Tells the system a widget is relevant at a specific date.
- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(_:kind:).md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(range:kind:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint, such as a calendar event.
- [RelevantContext.DateKind](relevantcontext/datekind.md)
  Values the system uses as additional context for time-based relevance clues.
- [static func date(from: Date, to: Date) -> RelevantContext](relevantcontext/date(from:to:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(interval:kind:))*