# getSupportedTimeTravelDirections(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Determines whether your complication can provide timeline entries for the future or the past.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Time Travel is no longer supported. Use CLKComplicationDataSource's getTimelineEndDateForComplication:withHandler: to specify forward timeline support.

## Declaration

```swift
optional func getSupportedTimeTravelDirections(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimeTravelDirections) -> Void)
```

```objc
- (void) getSupportedTimeTravelDirectionsForComplication:(CLKComplication *) complication withHandler:(void (^)(CLKComplicationTimeTravelDirections directions)) handler;
```

## Mentions

- [Loading future timeline events](../loading-future-timeline-events.md)

#### Discussion

The system calls this method to determine whether your app can provide future or past data entries for the specified complication type. Your implementation of this method must execute the block in the `handler` parameter and specify the supported directions.

Include the [`backward`](../clkcomplicationtimetraveldirections/backward.md) constant if your app provides a historical record of events that have occurred or information that was valid at specific times. For example, a music app could provide entries for songs that have already played.

Include the [`forward`](../clkcomplicationtimetraveldirections/forward.md) constant if your app is able to generate complication data tied to future dates. For example, a calendar app would provide entries for future meeting times.

In watchOS 7 and later, the system checks the value returned by [`getTimelineEndDate(for:withHandler:)`](./gettimelineenddate%28for,withhandler%29.md) instead. If the method returns a non-nil value, ClockKit attempts to bulk load future timeline entries. Otherwise, it only asks for the current timeline entry.

## Parameters

- `complication`: The complication tied to the request.
- `handler`: The handler to execute with the Time Travel directions. This block has no return value and takes the following parameter:

  - **directions**: The supported time travel directions. You may combine the values of the [`CLKComplicationTimeTravelDirections`](../clkcomplicationtimetraveldirections.md) type when specifying this value.

## Topics

### Time Travel Directions
- [struct CLKComplicationTimeTravelDirections](../clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.

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
- [struct CLKComplicationTimeTravelDirections](../clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](./gettimelinestartdate%28for,withhandler%29.md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getsupportedtimetraveldirections(for:withhandler:))*