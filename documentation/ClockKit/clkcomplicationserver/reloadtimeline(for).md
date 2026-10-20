# reloadTimeline(for:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Invalidates your existing timeline data and triggers an update session to reload it.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
func reloadTimeline(for complication: CLKComplication)
```

```objc
- (void) reloadTimelineForComplication:(CLKComplication *) complication;
```

## Mentions

- [Keeping your complications up to date](../keeping-your-complications-up-to-date.md)

#### Discussion

Call this method when your complication data is no longer accurate and needs to be completely replaced. ClockKit dumps any cached data and initiates a fresh update session to request new data from your complication data source. If your complication has already exceeded its allotted daily budget for execution time, calls to this method do nothing.

Call this method sparingly. If your existing complication data is still valid, consider calling the [`extendTimeline(for:)`](./extendtimeline%28for%29.md) method instead.

## See Also

### Updating Your Timeline Data
- [func extendTimeline(for: CLKComplication)](./extendtimeline%28for%29.md)
  Asks the system to extend the data in your complication’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/reloadtimeline(for:))*