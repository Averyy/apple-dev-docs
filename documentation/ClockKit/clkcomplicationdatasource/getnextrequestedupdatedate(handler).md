# getNextRequestedUpdateDate(handler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Gets the next time at which to update your complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`WKRefreshBackgroundTask`](../../WatchKit/wkrefreshbackgroundtask.md) instead.

## Declaration

```swift
optional func getNextRequestedUpdateDate(handler: @escaping (Date?) -> Void)
```

```objc
- (void) getNextRequestedUpdateDateWithHandler:(void (^)(NSDate *updateDate)) handler;
```

#### Discussion

Your implementation of this method must execute the block in the `handler` parameter and specify an appropriate date. Specify a date as far into the future as you can manage for your complications. ClockKit wakes up your complication at some point after the specified date to request new data. The exact time at which your complication runs isn’t guaranteed.

If your complication data changes before the specified update date, you can invalidate your complication data using the [`CLKComplicationServer`](../clkcomplicationserver.md) object.

If you don’t implement this method, ClockKit doesn’t schedule your complication for another update. You must trigger updates to your complication’s data manually by extending or reloading your timeline.

## Parameters

- `handler`: The handler to execute with the next date at which to run your complication code. This block has no return value and takes the following parameter:

  - **`updateDate`**: The date after which you’d like your complication to run again. If you specify `nil`, ClockKit doesn’t schedule a new update time for your complication. You can still trigger updates manually.

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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getnextrequestedupdatedate(handler:))*