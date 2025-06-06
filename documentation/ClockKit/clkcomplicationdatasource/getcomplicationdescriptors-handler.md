# getComplicationDescriptors(handler:)

**Framework**: ClockKit  
**Kind**: method

Returns the list of complication descriptors.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func complicationDescriptors() async -> [CLKComplicationDescriptor]
```

## Mentions

- [Declaring complications for your app](declaring-complications-for-your-app.md)

#### Discussion

ClockKit calls this method to determine the complications that an app supports. Implement this method to define your app’s complications. For example, a weather app may support different complications for the current condition, temperature, or chance of precipitation.

You can also use your implementation to customize the types of complications according to your app’s current data. For example, a weather app could provide separate complications for the user’s favorite locations.

In your data source’s implementation, create an array of [`CLKComplicationDescriptor`](clkcomplicationdescriptor.md) objects to represent the complications that your app supports, and then pass the array to the method’s handler.

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

To update the descriptors, call [`reloadComplicationDescriptors()`](clkcomplicationserver/reloadcomplicationdescriptors().md).

## Parameters

- `handler`: In your data source’s implementation, call the handler and pass the complication descriptors for your app. This block takes the following parameter:

## See Also

- [let CLKLaunchedTimelineEntryDateKey: String](clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
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
- [func getCurrentTimelineEntry(for: CLKComplication, withHandler: (CLKComplicationTimelineEntry?) -> Void)](clkcomplicationdatasource/getcurrenttimelineentry(for:withhandler:).md)
  Retrieves the timeline entry that you want to display now.
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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getcomplicationdescriptors(handler:))*