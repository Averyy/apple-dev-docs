# getLocalizableSampleTemplate(for:withHandler:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Gets a localizable template that shows sample data for the specified complication.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
optional func getLocalizableSampleTemplate(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTemplate?) -> Void)
```

```swift
optional func localizableSampleTemplate(for complication: CLKComplication) async -> CLKComplicationTemplate?
```

```objc
- (void) getLocalizableSampleTemplateForComplication:(CLKComplication *) complication withHandler:(void (^)(CLKComplicationTemplate *complicationTemplate)) handler;
```

## Mentions

- [Adding Placeholders for Your Complication](../adding-placeholders-for-your-complication.md)
- [Sharing an Apple Watch face](../sharing-an-apple-watch-face.md)

#### Discussion

The system calls this method once per supported complication when your extension is installed, and the results are cached. In your implementation, instantiate the appropriate template class and populate the resulting object with localized data. The data you supply should be fake, but it should reflect what your complication would normally look like.

If you pass `nil` to the handler, the system generates a default placeholder template from your app’s icon and name.

## Parameters

- `complication`: The complication tied to the request. Use the complication family information in this object to determine which set of templates are valid. For example, if the complication family is [`CLKComplicationFamily.utilitarianLarge`](../clkcomplicationfamily/utilitarianlarge.md), you’d instantiate the [`CLKComplicationTemplateUtilitarianLargeFlat`](../clkcomplicationtemplateutilitarianlargeflat.md) class for your template.
- `handler`: The handler to execute with the template. This block has no return value and takes the following parameter:

  - **template**: The template object containing your placeholder data. The data in this template is cached and displayed for your complication.

## See Also

### Related Documentation
- [class func localizableTextProvider(withStringsFileTextKey: String) -> Self](../clktextprovider/localizabletextprovider%28withstringsfiletextkey%29.md)
  Creates a localizable simple text provider using the strings file key for the text.
- [class func localizableTextProvider(withStringsFileFormatKey: String, textProviders: [CLKTextProvider]) -> Self](../clktextprovider/localizabletextprovider%28withstringsfileformatkey,textproviders%29.md)
  Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.
- [class func localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self](../clktextprovider/localizabletextprovider%28withstringsfiletextkey,shorttextkey%29.md)
  Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.
### Deprecated methods
- [let CLKLaunchedTimelineEntryDateKey: String](../clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](../clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
- [func getComplicationDescriptors(handler: ([CLKComplicationDescriptor]) -> Void)](./getcomplicationdescriptors%28handler%29.md)
  Returns the list of complication descriptors.
- [func handleSharedComplicationDescriptors([CLKComplicationDescriptor])](./handlesharedcomplicationdescriptors%28_%29.md)
  Informs the app about complications from a shared watch face.
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

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/getlocalizablesampletemplate(for:withhandler:))*