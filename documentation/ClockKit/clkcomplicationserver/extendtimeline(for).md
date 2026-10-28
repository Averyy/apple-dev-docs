# extendTimeline(for:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Asks the system to extend the data in your complication’s timeline.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
func extendTimeline(for complication: CLKComplication)
```

```objc
- (void) extendTimelineForComplication:(CLKComplication *) complication;
```

## Mentions

- [Keeping your complications up to date](../keeping-your-complications-up-to-date.md)

## Discussion

Call this method when your existing complication data is still valid and you’ve new data to add to the end of your timeline. ClockKit initiates an update session to request the additional data from your complication data source. If your complication has already exceeded its allotted daily budget for execution time, calls to this method do nothing.

## Parameters

- `complication`: The complication whose data you want to extend.

## See Also

### Updating Your Timeline Data
- [func reloadTimeline(for: CLKComplication)](./reloadtimeline%28for%29.md)
  Invalidates your existing timeline data and triggers an update session to reload it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/extendtimeline(for:))*