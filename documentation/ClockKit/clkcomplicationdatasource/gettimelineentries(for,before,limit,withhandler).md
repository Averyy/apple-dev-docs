# getTimelineEntries(for:before:limit:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Retrieves past timeline entries for the complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Time Travel and backwards extension of timelines are no longer supported.

## Declaration

```swift
optional func getTimelineEntries(for complication: CLKComplication, before date: Date, limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Void)
```

```objc
- (void) getTimelineEntriesForComplication:(CLKComplication *) complication beforeDate:(NSDate *) date limit:(NSUInteger) limit withHandler:(void (^)(NSArray<CLKComplicationTimelineEntry *> *entries)) handler;
```

#### Discussion

Only implement this method if your app supports Time Travel on watchOS 4 or earlier.

Use this method to build an array of timeline entries with your app’s past data. Each timeline entry contains the data and the date at which that data is valid. Don’t provide entries with dates after the one in the `date` parameter, and limit the number of entries you create to the value in the `limit` parameter.

The array you return must start in the past and extend forward into time, ending no later than the date specified in the `date` parameter. Each successive entry in the array must come after the one before it. Entries must be greater than one minute apart. If two entries are less than one minute apart, ClockKit discards one of the entries.

Don’t include the current entry in your array. That entry is retrieved separately using the [`getCurrentTimelineEntry(for:withHandler:)`](./getcurrenttimelineentry%28for,withhandler%29.md) method.

If you don’t implement this method, ClockKit doesn’t try to add earlier entries to the timeline.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid.
- `date`: The end date for providing past entries. The dates for your timeline entries should occur before this date and be as close to the date as possible.
- `limit`: The maximum number of entries to provide.
- `handler`: The handler to execute with the past timeline data. This block has no return value and takes the following parameter:

  - **`entries`**: An array of [`CLKComplicationTimelineEntry`](../clkcomplicationtimelineentry.md) objects representing the past data. The number of entries in the array must be less than or equal to the value in the `limit` parameter. If you specify `nil`, ClockKit doesn’t try to extend the timeline further.

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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/gettimelineentries(for:before:limit:withhandler:))*