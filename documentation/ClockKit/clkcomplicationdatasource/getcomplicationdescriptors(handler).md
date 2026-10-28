# getComplicationDescriptors(handler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Returns the list of complication descriptors.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
optional func getComplicationDescriptors(handler: @escaping ([CLKComplicationDescriptor]) -> Void)
```

```swift
optional func complicationDescriptors() async -> [CLKComplicationDescriptor]
```

```objc
- (void) getComplicationDescriptorsWithHandler:(void (^)(NSArray<CLKComplicationDescriptor *> *)) handler;
```

## Mentions

- [Declaring complications for your app](../declaring-complications-for-your-app.md)

## Discussion

ClockKit calls this method to determine the complications that an app supports. Implement this method to define your app’s complications. For example, a weather app may support different complications for the current condition, temperature, or chance of precipitation.

You can also use your implementation to customize the types of complications according to your app’s current data. For example, a weather app could provide separate complications for the user’s favorite locations.

In your data source’s implementation, create an array of [`CLKComplicationDescriptor`](../clkcomplicationdescriptor.md) objects to represent the complications that your app supports, and then pass the array to the method’s handler.

```swift
func getComplicationDescriptors(handler: @escaping ([CLKComplicationDescriptor]) -> Void) {
    
    let mySupportedFamilies = CLKComplicationFamily.allCases

    // Create the condition descriptor.
    let conditionDescriptor = CLKComplicationDescriptor(
        identifier: complicationConditionIdentifier,
        displayName: "Weather Condition",
        supportedFamilies: mySupportedFamilies)

    // Create the temperature descriptor.
    let temperatureDescriptor = CLKComplicationDescriptor(
        identifier: complicationTemperatureIdentifier,
        displayName: "Temperature",
        supportedFamilies: mySupportedFamilies)

    // Create the precipitation descriptor.
    let precipitationDescriptor = CLKComplicationDescriptor(
        identifier: complicationPrecipitationIdentifier,
        displayName: "Percipitation",
        supportedFamilies: mySupportedFamilies)
    
    // Call the handler and pass an array of descriptors.
    handler([conditionDescriptor,
             temperatureDescriptor,
             precipitationDescriptor])
}
```

In addition to defining a unique type of complication, each descriptor also defines the families that the complication supports. Each descriptor appears as a separate complication on the Apple Watch’s face customization screen.

The complications appear in the same order as the descriptor array. When the user configures a complication, the picker shows the first three items from the array that support the complication’s family. If there are more than three, the picker displays a More button to provide access to the additional complications.

To update the descriptors, call [`reloadComplicationDescriptors()`](../clkcomplicationserver/reloadcomplicationdescriptors%28%29.md).

## Parameters

- `handler`: In your data source’s implementation, call the handler and pass the complication descriptors for your app. This block takes the following parameter:

  - **`descriptors`**: An array containing your app’s complication descriptors.

## See Also

### Deprecated methods
- [let CLKLaunchedTimelineEntryDateKey: String](../clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](../clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
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
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](./gettimelinestartdate%28for,withhandler%29.md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getcomplicationdescriptors(handler:))*