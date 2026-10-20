# date(_:)

**Framework**: RelevanceKit  
**Kind**: method  
**Role**: Type Method

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

Let the system know that a widget is most relevant to a person on a specific date. For example, an app people use to follow sport events might provide the start of a match or a live broadcast. If you know when the widget isn’t relevant anymore, use [`date(interval:kind:)`](./date%28interval,kind%29.md).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [Increasing the visibility of widgets in Smart Stacks](../../WidgetKit/widget-suggestions-in-smart-stacks.md).

## Parameters

- `exact`: The time the widget is most relevant to a person.

## See Also

### Time clues
- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](./date%28_,kind%29.md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext](./date%28interval,kind%29.md)
  Tells the system a widget is relevant for a time interval and provides an additional contextual hint.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](./date%28range,kind%29.md)
  Tells the system a widget is relevant for a known date range and provides an additional contextual hint.
- [RelevantContext.DateKind](./datekind.md)
  Values the system uses as additional context for time-based relevance clues.
- [static func date(from: Date, to: Date) -> RelevantContext](./date%28from,to%29.md)
  Tells the system a widget is relevant between two dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(_:))*