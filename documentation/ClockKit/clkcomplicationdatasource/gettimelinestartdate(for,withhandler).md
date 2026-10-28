# getTimelineStartDate(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the earliest date for which your complication is prepared to supply data.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Time Travel and backwards extension of timelines are no longer supported.

## Declaration

```swift
optional func getTimelineStartDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Void)
```

```objc
- (void) getTimelineStartDateForComplication:(CLKComplication *) complication withHandler:(void (^)(NSDate *date)) handler;
```

## Discussion

Only implement this method if your app supports Time Travel on watchOS 4 or earlier.

Your implementation of this method must execute the block in the `handler` parameter and specify the earliest date for which you can supply timeline entries. If you don’t support displaying past data using Time Travel, specify the current date.

If you don’t implement this method, ClockKit doesn’t attempt to retrieve timeline entries before the current entry.

## Parameters

- `complication`: The complication tied to the request.
- `handler`: The handler to execute with the start date. This block has no return value and takes the following parameter:

  - **`date`**: The start date for your data. For times before this date, WatchKit dims your data to indicate that the timeline doesn’t continue. If you specify `nil`, ClockKit doesn’t ask for any more past data.

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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/gettimelinestartdate(for:withhandler:))*