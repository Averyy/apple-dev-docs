# getPlaceholderTemplate(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Gets a static template to display in the selection screen for your complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`getLocalizableSampleTemplate(for:withHandler:)`](./getlocalizablesampletemplate%28for,withhandler%29.md) instead.

## Declaration

```swift
optional func getPlaceholderTemplate(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTemplate?) -> Void)
```

```objc
- (void) getPlaceholderTemplateForComplication:(CLKComplication *) complication withHandler:(void (^)(CLKComplicationTemplate *complicationTemplate)) handler;
```

## Discussion

When your app is first launched, ClockKit calls this method to retrieve an appropriate placeholder template for your complication. In the customization screen for the clock face, your placeholder template is displayed to the user during the selection process. The contents of the placeholder aren’t updated and are meant to convey the type of data your complication displays. They don’t need to convey actual user data.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid.
- `handler`: The handler to execute with the template. This block has no return value and takes the following parameter:

  - **template**: The template object containing your placeholder data. The data in this template is cached and displayed for your complication.

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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getplaceholdertemplate(for:withhandler:))*