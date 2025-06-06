# CLKDefaultComplicationIdentifier

**Framework**: ClockKit  
**Kind**: var

An identifier representing a default complication.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
let CLKDefaultComplicationIdentifier: String
```

#### Discussion

The system assigns a [`CLKDefaultComplicationIdentifier`](clkdefaultcomplicationidentifier.md) value to the complication’s `identifier` property, whenever a specific identifier is unavailable. For example, ClockKit uses default type identifiers to represent the type on complications designed for watchOS 6 or earlier. It also uses the default type for complications from a shared watch face, when the sender chose to not include complication data in the shared watch face.

If your app supports multiple complications per family, you must check for [`CLKDefaultComplicationIdentifier`](clkdefaultcomplicationidentifier.md) values in your data source’s [`getCurrentTimelineEntry(for:withHandler:)`](clkcomplicationdatasource/getcurrenttimelineentry(for:withhandler:).md) and [`getTimelineEntries(for:after:limit:withHandler:)`](clkcomplicationdatasource/gettimelineentries(for:after:limit:withhandler:).md) methods. If you receive a [`CLKDefaultComplicationIdentifier`](clkdefaultcomplicationidentifier.md), return generic entries for the specified family.

```swift
switch complication.identifier {
    
case CLKDefaultComplicationIdentifier:
    templateOrNil = myGetConditionTemplate(for: complication, date: date)
    
case ComplicationTypeTemperatureIdentifier, CLKDefaultComplicationTypeIdentifier:
    templateOrNil = myGetTemperatureTemplate(for: complication, date: date)
    
case ComplicationTypePrecipitationPercentageIdentifier:
    templateOrNil = myGetPrecipitationPercentageTemplate(for: complication, date: date)
    
default:
    print("*** Unrecognized Complication Type ***")
    return nil
}
```

## See Also

- [Migrating ClockKit complications to WidgetKit](../WidgetKit/Converting-A-ClockKit-App.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [protocol CLKComplicationDataSource](clkcomplicationdatasource.md)
  A protocol that provides ClockKit with information about your complication.
- [class CLKComplicationDescriptor](clkcomplicationdescriptor.md)
  A descriptor that defines a complication and the families that it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdefaultcomplicationidentifier)*