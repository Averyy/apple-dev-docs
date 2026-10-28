# CLKLaunchedTimelineEntryDateKey

**Framework**: ClockKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates the date when the system launched the complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
let CLKLaunchedTimelineEntryDateKey: String
```

```c
extern NSString * const CLKLaunchedTimelineEntryDateKey;
```

## Discussion

The value of this key is an [`NSDate`](../Foundation/nsdate.md) object. When the user taps your complication, ClockKit includes this key in the dictionary that it passes to the extension delegate’s [`handleUserActivity(_:)`](../WatchKit/wkextensiondelegate/handleuseractivity%28_%29.md) method.

## See Also

### Deprecated methods
- [let CLKLaunchedComplicationIdentifierKey: String](./clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
- [func getComplicationDescriptors(handler: ([CLKComplicationDescriptor]) -> Void)](./clkcomplicationdatasource/getcomplicationdescriptors%28handler%29.md)
  Returns the list of complication descriptors.
- [func handleSharedComplicationDescriptors([CLKComplicationDescriptor])](./clkcomplicationdatasource/handlesharedcomplicationdescriptors%28_%29.md)
  Informs the app about complications from a shared watch face.
- [func getLocalizableSampleTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./clkcomplicationdatasource/getlocalizablesampletemplate%28for,withhandler%29.md)
  Gets a localizable template that shows sample data for the specified complication.
- [func getPrivacyBehavior(for: CLKComplication, withHandler: (CLKComplicationPrivacyBehavior) -> Void)](./clkcomplicationdatasource/getprivacybehavior%28for,withhandler%29.md)
  Returns the privacy behavior for the specified complication.
- [enum CLKComplicationPrivacyBehavior](./clkcomplicationprivacybehavior.md)
  Constants indicating the complication behavior when the Apple Watch is locked.
- [func getAlwaysOnTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./clkcomplicationdatasource/getalwaysontemplate%28for,withhandler%29.md)
  Returns the template to use during Always On.
- [func getTimelineEndDate(for: CLKComplication, withHandler: (Date?) -> Void)](./clkcomplicationdatasource/gettimelineenddate%28for,withhandler%29.md)
  Retrieves the last date for the data that your app can supply.
- [func getCurrentTimelineEntry(for: CLKComplication, withHandler: (CLKComplicationTimelineEntry?) -> Void)](./clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md)
  Retrieves the timeline entry that you want to display now.
- [func getTimelineEntries(for: CLKComplication, after: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Void)](./clkcomplicationdatasource/gettimelineentries%28for,after,limit,withhandler%29.md)
  Retrieves future timeline entries for the complication.
- [func getTimelineAnimationBehavior(for: CLKComplication, withHandler: (CLKComplicationTimelineAnimationBehavior) -> Void)](./clkcomplicationdatasource/gettimelineanimationbehavior%28for,withhandler%29.md)
  Gets the animation behavior when transitioning between timeline entries.
- [enum CLKComplicationTimelineAnimationBehavior](./clkcomplicationtimelineanimationbehavior.md)
  Constants indicating the animation behavior during Time Travel.
- [func getSupportedTimeTravelDirections(for: CLKComplication, withHandler: (CLKComplicationTimeTravelDirections) -> Void)](./clkcomplicationdatasource/getsupportedtimetraveldirections%28for,withhandler%29.md)
  Determines whether your complication can provide timeline entries for the future or the past.
- [struct CLKComplicationTimeTravelDirections](./clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](./clkcomplicationdatasource/gettimelinestartdate%28for,withhandler%29.md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clklaunchedtimelineentrydatekey)*