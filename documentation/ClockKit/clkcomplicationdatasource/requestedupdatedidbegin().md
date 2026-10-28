# requestedUpdateDidBegin()

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Indicates that a requested update has begun so that you’ve an opportunity to extend or reload your timeline.

**Availability**:
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`WKRefreshBackgroundTask`](../../WatchKit/wkrefreshbackgroundtask.md) instead.

## Declaration

```swift
optional func requestedUpdateDidBegin()
```

```objc
- (void) requestedUpdateDidBegin;
```

## Discussion

When the date returned by the [`getNextRequestedUpdateDate(handler:)`](./getnextrequestedupdatedate%28handler%29.md) method of your data source passes, ClockKit begins a scheduled update of your complication. At the start of that update, it calls this method or the [`requestedUpdateBudgetExhausted()`](./requestedupdatebudgetexhausted%28%29.md) method to let you know that the requested update has begun. These methods are your opportunity to tell ClockKit whether or not you’ve new data to add to your timeline.

If you’ve new data for your timeline, your implementation of this method should call the [`reloadTimeline(for:)`](../clkcomplicationserver/reloadtimeline%28for%29.md) or [`extendTimeline(for:)`](../clkcomplicationserver/extendtimeline%28for%29.md) method of the complication server. ClockKit doesn’t ask your data source for new timeline entries unless you call one of those methods. If you do nothing or don’t implement this method, ClockKit calls only the [`getNextRequestedUpdateDate(handler:)`](./getnextrequestedupdatedate%28handler%29.md) of your data source to fetch a new update time.

## See Also

### Deprecated methods
- [let CLKLaunchedTimelineEntryDateKey: String](../clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](../clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
- [func getComplicationDescriptors(handler: ([CLKComplicationDescriptor]) -> Void)](./getcomplicationdescriptors%28handler%29.md)
  Returns the list of complication descriptors.
- [func handleSharedComplicationDescriptors([CLKComplicationDescriptor])](./handlesharedcomplicationdescriptors%28_%29.md)
  Informs the app about complications from a shared watch face.
- [func getLocalizableSampleTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./getlocalizablesampletemplate%28for,withhandler%29.md)
  Gets a localizable template that shows sample data for the specified complication.
- [func getPrivacyBehavior(for: CLKComplication, withHandler: (CLKComplicationPrivacyBehavior) -> Void)](./getprivacybehavior%28for,withhandler%29.md)
  Returns the privacy behavior for the specified complication.
- [enum CLKComplicationPrivacyBehavior](../clkcomplicationprivacybehavior.md)
  Constants indicating the complication behavior when the Apple Watch is locked.
- [func getAlwaysOnTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./getalwaysontemplate%28for,withhandler%29.md)
  Returns the template to use during Always On.
- [func getTimelineEndDate(for: CLKComplication, withHandler: (Date?) -> Void)](./gettimelineenddate%28for,withhandler%29.md)
  Retrieves the last date for the data that your app can supply.
- [func getCurrentTimelineEntry(for: CLKComplication, withHandler: (CLKComplicationTimelineEntry?) -> Void)](./getcurrenttimelineentry%28for,withhandler%29.md)
  Retrieves the timeline entry that you want to display now.
- [func getTimelineEntries(for: CLKComplication, after: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Void)](./gettimelineentries%28for,after,limit,withhandler%29.md)
  Retrieves future timeline entries for the complication.
- [func getTimelineAnimationBehavior(for: CLKComplication, withHandler: (CLKComplicationTimelineAnimationBehavior) -> Void)](./gettimelineanimationbehavior%28for,withhandler%29.md)
  Gets the animation behavior when transitioning between timeline entries.
- [enum CLKComplicationTimelineAnimationBehavior](../clkcomplicationtimelineanimationbehavior.md)
  Constants indicating the animation behavior during Time Travel.
- [func getSupportedTimeTravelDirections(for: CLKComplication, withHandler: (CLKComplicationTimeTravelDirections) -> Void)](./getsupportedtimetraveldirections%28for,withhandler%29.md)
  Determines whether your complication can provide timeline entries for the future or the past.
- [struct CLKComplicationTimeTravelDirections](../clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/requestedupdatedidbegin())*