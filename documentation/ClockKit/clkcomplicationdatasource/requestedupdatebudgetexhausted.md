# requestedUpdateBudgetExhausted()

**Framework**: ClockKit  
**Kind**: method

Indicates that your complication’s time budget is exhausted.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func requestedUpdateBudgetExhausted()
```

#### Discussion

When the date returned by the [`getNextRequestedUpdateDate(handler:)`](clkcomplicationdatasource/getnextrequestedupdatedate(handler:).md) method of your data source passes, ClockKit begins a scheduled update of your complication. At the start of that update, it calls this method or the [`requestedUpdateDidBegin()`](clkcomplicationdatasource/requestedupdatedidbegin().md) method to let you know that the requested update has begun. These methods are your opportunity to tell ClockKit whether or not you’ve new data to add to your timeline. When this method is called, it’s your last opportunity to update your timeline until its budget is replenished.

If you’ve new data for your timeline, your implementation of this method should call the [`reloadTimeline(for:)`](clkcomplicationserver/reloadtimeline(for:).md) or [`extendTimeline(for:)`](clkcomplicationserver/extendtimeline(for:).md) method of the complication server. ClockKit doesn’t ask your data source for new timeline entries unless you call one of those methods. If you do nothing or don’t implement this method, ClockKit calls only the [`getNextRequestedUpdateDate(handler:)`](clkcomplicationdatasource/getnextrequestedupdatedate(handler:).md) of your data source to fetch a new update time.

## See Also

- [let CLKLaunchedTimelineEntryDateKey: String](clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
- [func getComplicationDescriptors(handler: ([CLKComplicationDescriptor]) -> Void)](clkcomplicationdatasource/getcomplicationdescriptors(handler:).md)
  Returns the list of complication descriptors.
- [func handleSharedComplicationDescriptors([CLKComplicationDescriptor])](clkcomplicationdatasource/handlesharedcomplicationdescriptors(_:).md)
  Informs the app about complications from a shared watch face.
- [func getLocalizableSampleTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](clkcomplicationdatasource/getlocalizablesampletemplate(for:withhandler:).md)
  Gets a localizable template that shows sample data for the specified complication.
- [func getPrivacyBehavior(for: CLKComplication, withHandler: (CLKComplicationPrivacyBehavior) -> Void)](clkcomplicationdatasource/getprivacybehavior(for:withhandler:).md)
  Returns the privacy behavior for the specified complication.
- [enum CLKComplicationPrivacyBehavior](clkcomplicationprivacybehavior.md)
  Constants indicating the complication behavior when the Apple Watch is locked.
- [func getAlwaysOnTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](clkcomplicationdatasource/getalwaysontemplate(for:withhandler:).md)
  Returns the template to use during Always On.
- [func getTimelineEndDate(for: CLKComplication, withHandler: (Date?) -> Void)](clkcomplicationdatasource/gettimelineenddate(for:withhandler:).md)
  Retrieves the last date for the data that your app can supply.
- [func getCurrentTimelineEntry(for: CLKComplication, withHandler: (CLKComplicationTimelineEntry?) -> Void)](clkcomplicationdatasource/getcurrenttimelineentry(for:withhandler:).md)
  Retrieves the timeline entry that you want to display now.
- [func getTimelineEntries(for: CLKComplication, after: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Void)](clkcomplicationdatasource/gettimelineentries(for:after:limit:withhandler:).md)
  Retrieves future timeline entries for the complication.
- [func getTimelineAnimationBehavior(for: CLKComplication, withHandler: (CLKComplicationTimelineAnimationBehavior) -> Void)](clkcomplicationdatasource/gettimelineanimationbehavior(for:withhandler:).md)
  Gets the animation behavior when transitioning between timeline entries.
- [enum CLKComplicationTimelineAnimationBehavior](clkcomplicationtimelineanimationbehavior.md)
  Constants indicating the animation behavior during Time Travel.
- [func getSupportedTimeTravelDirections(for: CLKComplication, withHandler: (CLKComplicationTimeTravelDirections) -> Void)](clkcomplicationdatasource/getsupportedtimetraveldirections(for:withhandler:).md)
  Determines whether your complication can provide timeline entries for the future or the past.
- [struct CLKComplicationTimeTravelDirections](clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/requestedupdatebudgetexhausted())*