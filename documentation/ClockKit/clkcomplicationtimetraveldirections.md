# CLKComplicationTimeTravelDirections

**Framework**: ClockKit  
**Kind**: struct

Constants indicating the supported time travel directions, if any.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
struct CLKComplicationTimeTravelDirections
```

## Topics

### Constants
- [static var forward: CLKComplicationTimeTravelDirections](clkcomplicationtimetraveldirections/forward.md)
  Future data support. Use this option when it makes sense to provide future data for your complication.
- [static var backward: CLKComplicationTimeTravelDirections](clkcomplicationtimetraveldirections/backward.md)
  Past data support. Use this option when it makes sense to provide past data for your complication.
### Initializers
- [init(rawValue: UInt)](clkcomplicationtimetraveldirections/init(rawvalue:).md)
  Returns a new [`CLKComplicationTimeTravelDirections`](clkcomplicationtimetraveldirections.md) instance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](clkcomplicationdatasource/gettimelinestartdate(for:withhandler:).md)
  Retrieves the earliest date for which your complication is prepared to supply data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimetraveldirections)*