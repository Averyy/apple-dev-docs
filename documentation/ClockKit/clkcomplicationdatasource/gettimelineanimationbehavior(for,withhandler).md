# getTimelineAnimationBehavior(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Gets the animation behavior when transitioning between timeline entries.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
optional func getTimelineAnimationBehavior(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineAnimationBehavior) -> Void)
```

```swift
optional func timelineAnimationBehavior(for complication: CLKComplication) async -> CLKComplicationTimelineAnimationBehavior
```

```objc
- (void) getTimelineAnimationBehaviorForComplication:(CLKComplication *) complication withHandler:(void (^)(CLKComplicationTimelineAnimationBehavior behavior)) handler;
```

## Discussion

Only implement this method if your app supports Time Travel on watchOS 4 or earlier.

Implement this method if you want ClockKit to create transition animations between your timeline entries during Time Travel. Transition animations create softer transitions between different entries. You might use them when the value of an entry changes dramatically or when you change the template you’re using.

You can use group identifiers to eliminate transition animations between specific timeline entries. When animations are enabled, ClockKit creates animations only when the group identifier of successive timeline entries is different.

If you don’t implement this method, ClockKit doesn’t animate the transitions between timeline entries.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid.
- `handler`: The handler to execute with the animation behavior. This block has no return value and takes the following parameter:

  - **behavior**: The animation behavior to use. For a list of possible values, see [`CLKComplicationTimelineAnimationBehavior`](../clkcomplicationtimelineanimationbehavior.md).

## Topics

### Animation Behaviors
- [enum CLKComplicationTimelineAnimationBehavior](../clkcomplicationtimelineanimationbehavior.md)
  Constants indicating the animation behavior during Time Travel.

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
- [enum CLKComplicationTimelineAnimationBehavior](../clkcomplicationtimelineanimationbehavior.md)
  Constants indicating the animation behavior during Time Travel.
- [func getSupportedTimeTravelDirections(for: CLKComplication, withHandler: (CLKComplicationTimeTravelDirections) -> Void)](./getsupportedtimetraveldirections%28for,withhandler%29.md)
  Determines whether your complication can provide timeline entries for the future or the past.
- [struct CLKComplicationTimeTravelDirections](../clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](./gettimelinestartdate%28for,withhandler%29.md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/gettimelineanimationbehavior(for:withhandler:))*