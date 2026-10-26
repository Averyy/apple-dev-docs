# CLKComplicationServer

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

An object that manages the active complications for an app.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationServer
```

```objc
@interface CLKComplicationServer : NSObject
```

#### Overview

Don’t create instances of this class directly. Instead, use the shared object to fetch information about your active complications and to invalidate or extend the data for a specific complication. You can also use it to get information about the minimum and maximum dates for which you need to provide data to support Time Travel.

## Topics

### Getting the Complication Server
- [class func sharedInstance() -> Self](./clkcomplicationserver/sharedinstance%28%29.md)
  Returns the shared complication server.
### Getting the Active Complications
- [var activeComplications: [CLKComplication]?](./clkcomplicationserver/activecomplications.md)
  The active complications for the current app.
### Updating Your Timeline Data
- [func reloadTimeline(for: CLKComplication)](./clkcomplicationserver/reloadtimeline%28for%29.md)
  Invalidates your existing timeline data and triggers an update session to reload it.
- [func extendTimeline(for: CLKComplication)](./clkcomplicationserver/extendtimeline%28for%29.md)
  Asks the system to extend the data in your complication’s timeline.
### Updating Complication Types
- [func reloadComplicationDescriptors()](./clkcomplicationserver/reloadcomplicationdescriptors%28%29.md)
  Reloads the complication descriptors from the complication data source.
### Getting the Time Travel Boundaries
- [var earliestTimeTravelDate: Date](./clkcomplicationserver/earliesttimetraveldate.md)
  The earliest Time Travel date for which you should provide data.
- [var latestTimeTravelDate: Date](./clkcomplicationserver/latesttimetraveldate.md)
  The latest date supported by Time Travel.
### Receiving Change Notifications
- [CLKComplicationServerActiveComplicationsDidChangeNotification](./clkcomplicationserveractivecomplicationsdidchangenotification.md)
  Posted when the set of active complications changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Other Symbols
- [class CLKComplication](./clkcomplication.md)
  Metadata about a custom complication.
- [class CLKComplicationTimelineEntry](./clkcomplicationtimelineentry.md)
  A container for the complication template object to display and the time to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver)*