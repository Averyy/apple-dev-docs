# getTimelineEntries(for:after:limit:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Retrieves future timeline entries for the complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
optional func getTimelineEntries(for complication: CLKComplication, after date: Date, limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Void)
```

```swift
optional func timelineEntries(for complication: CLKComplication, after date: Date, limit: Int) async -> [CLKComplicationTimelineEntry]?
```

```objc
- (void) getTimelineEntriesForComplication:(CLKComplication *) complication afterDate:(NSDate *) date limit:(NSUInteger) limit withHandler:(void (^)(NSArray<CLKComplicationTimelineEntry *> *entries)) handler;
```

## Mentions

- [Loading future timeline events](../loading-future-timeline-events.md)
- [Sharing an Apple Watch face](../sharing-an-apple-watch-face.md)

## Discussion

Use this method to build an array of timeline entries with your app’s future data. Each timeline entry contains the data and the date at which that data is valid. Don’t provide entries that occur before the date in the `date` parameter, and limit the number of entries you create to the value in the `limit` parameter.

The array you return must start after the date specified in the `date` parameter and extend forward in time. Each successive entry in the array must come after the one before it. Entries must be greater than one minute apart. If two entries are less than one minute apart, ClockKit discards one of the entries.

Don’t include the current entry in your array. That entry is retrieved separately using the [`getCurrentTimelineEntry(for:withHandler:)`](./getcurrenttimelineentry%28for,withhandler%29.md) method.

If you don’t implement this method, ClockKit doesn’t try to add later entries to the timeline.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid.
- `date`: The starting date for providing future entries. The dates for your timeline entries should occur after this date and be as close to the date as possible.
- `limit`: The maximum number of entries to provide.
- `handler`: The handler to execute with the future timeline data. This block has no return value and takes the following parameter:

  - **`entries`**: An array of [`CLKComplicationTimelineEntry`](../clkcomplicationtimelineentry.md) objects representing the future data. The number of entries in the array must be less than or equal to the value in the `limit` parameter. If you specify `nil`, ClockKit doesn’t try to extend the timeline further.

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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/gettimelineentries(for:after:limit:withhandler:))*