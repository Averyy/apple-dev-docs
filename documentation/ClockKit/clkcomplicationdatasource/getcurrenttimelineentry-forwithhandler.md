# getCurrentTimelineEntry(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Required**: Yes

Retrieves the timeline entry that you want to display now.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func currentTimelineEntry(for complication: CLKComplication) async -> CLKComplicationTimelineEntry?
```

## Mentions

- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)
- [Loading future timeline events](loading-future-timeline-events.md)

#### Discussion

Your implementation of this method must create a timeline entry with the data to display right now. Assign a date to your timeline entry that reflects the current time or a time before the current time. If your complication supports past timeline entries, the entry you return from this method must come after all past entries that you provide using the [`getTimelineEntries(for:before:limit:withHandler:)`](clkcomplicationdatasource/gettimelineentries(for:before:limit:withhandler:).md) method.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid.
- `handler`: The handler to execute with the current data. This block has no return value and takes the following parameter:

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
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](clkcomplicationdatasource/gettimelinestartdate(for:withhandler:).md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getcurrenttimelineentry(for:withhandler:))*