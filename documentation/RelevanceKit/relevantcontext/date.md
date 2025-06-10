# date(_:)

**Framework**: RelevanceKit  
**Kind**: method

Tells the system a widget is relevant at a specific date.

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
static func date(_ exact: Date) -> RelevantContext
```

#### Return Value

A contextual clue that the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch.

#### Discussion

Let the system know that a widget is most relevant to a person on a specific date. For example, an app people use to follow sport events might provide the start of a match or a live broadcast. If you know when the widget isn’t relevant anymore, use [`date(interval:kind:)`](relevantcontext/date(interval:kind:).md).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Parameters

- `exact`: The time the widget is most relevant to a person.

## See Also

- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(_:kind:).md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(interval:kind:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint, such as a calendar event.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(range:kind:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint, such as a calendar event.
- [RelevantContext.DateKind](relevantcontext/datekind.md)
  Values the system uses as additional context for time-based relevance clues.
- [static func date(from: Date, to: Date) -> RelevantContext](relevantcontext/date(from:to:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(_:))*