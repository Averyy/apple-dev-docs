# getLocalizableSampleTemplate(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method

Gets a localizable template that shows sample data for the specified complication.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor
optional func localizableSampleTemplate(for complication: CLKComplication) async -> CLKComplicationTemplate?
```

## Mentions

- [Adding Placeholders for Your Complication](adding-placeholders-for-your-complication.md)
- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)

#### Discussion

The system calls this method once per supported complication when your extension is installed, and the results are cached. In your implementation, instantiate the appropriate template class and populate the resulting object with localized data. The data you supply should be fake, but it should reflect what your complication would normally look like.

If you pass `nil` to the handler, the system generates a default placeholder template from your app’s icon and name.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid. For example, if the complication family is  , you’d instantiate the   class for your template.
- `handler`: The handler to execute with the template. This block has no return value and takes the following parameter:

## See Also

- [class func localizableTextProvider(withStringsFileTextKey: String) -> Self](clktextprovider/localizabletextprovider(withstringsfiletextkey:).md)
  Creates a localizable simple text provider using the strings file key for the text.
- [class func localizableTextProvider(withStringsFileFormatKey: String, textProviders: [CLKTextProvider]) -> Self](clktextprovider/localizabletextprovider(withstringsfileformatkey:textproviders:).md)
  Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.
- [class func localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self](clktextprovider/localizabletextprovider(withstringsfiletextkey:shorttextkey:).md)
  Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.
- [let CLKLaunchedTimelineEntryDateKey: String](clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
- [func getComplicationDescriptors(handler: ([CLKComplicationDescriptor]) -> Void)](clkcomplicationdatasource/getcomplicationdescriptors(handler:).md)
  Returns the list of complication descriptors.
- [func handleSharedComplicationDescriptors([CLKComplicationDescriptor])](clkcomplicationdatasource/handlesharedcomplicationdescriptors(_:).md)
  Informs the app about complications from a shared watch face.
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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getlocalizablesampletemplate(for:withhandler:))*