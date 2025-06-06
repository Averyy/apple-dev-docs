# reloadTimeline(for:)

**Framework**: ClockKit  
**Kind**: method

Invalidates your existing timeline data and triggers an update session to reload it.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func reloadTimeline(for complication: CLKComplication)
```

## Mentions

- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)

#### Discussion

Call this method when your complication data is no longer accurate and needs to be completely replaced. ClockKit dumps any cached data and initiates a fresh update session to request new data from your complication data source. If your complication has already exceeded its allotted daily budget for execution time, calls to this method do nothing.

Call this method sparingly. If your existing complication data is still valid, consider calling the [`extendTimeline(for:)`](clkcomplicationserver/extendtimeline(for:).md) method instead.

## See Also

- [func extendTimeline(for: CLKComplication)](clkcomplicationserver/extendtimeline(for:).md)
  Asks the system to extend the data in your complication’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/reloadtimeline(for:))*