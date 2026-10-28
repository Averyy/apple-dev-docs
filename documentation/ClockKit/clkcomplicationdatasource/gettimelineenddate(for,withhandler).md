# getTimelineEndDate(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the last date for the data that your app can supply.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
optional func getTimelineEndDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Void)
```

```swift
optional func timelineEndDate(for complication: CLKComplication) async -> Date?
```

```objc
- (void) getTimelineEndDateForComplication:(CLKComplication *) complication withHandler:(void (^)(NSDate *date)) handler;
```

## Mentions

- [Loading future timeline events](../loading-future-timeline-events.md)
- [Sharing an Apple Watch face](../sharing-an-apple-watch-face.md)

## Discussion

Your implementation of this method must execute the block in the handler parameter and specify the date. If your application can’t provide future timeline entries, specify the current date.

If you don’t implement this method, ClockKit doesn’t attempt to retrieve timeline entries after the current entry.

> ❗ **Important**:  In watchOS 6 and earlier, if you passed `nil` to the completion handler, ClockKit set the timeline end date to [`distantFuture`](../../Foundation/nsdate/distantfuture.md). In watchOS 7 and later, it assumes your app can’t provide future data, and only asks for the current timeline entry.

## Parameters

- `complication`: The complication tied to the request.
- `handler`: The handler to execute with the end date. This block has no return value and takes the following parameter:

  - **`date`**: The end date for your data. If you specify `nil`, ClockKit doesn’t ask for any more future data.

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
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](./gettimelinestartdate%28for,withhandler%29.md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/gettimelineenddate(for:withhandler:))*