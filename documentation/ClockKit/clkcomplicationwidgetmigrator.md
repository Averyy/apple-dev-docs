# CLKComplicationWidgetMigrator

**Framework**: ClockKit  
**Kind**: protocol

A protocol that maps ClockKit complications to their WidgetKit replacements.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
protocol CLKComplicationWidgetMigrator : NSObjectProtocol
```

## Topics

### Migrating complications
- [func getWidgetConfiguration(from: CLKComplicationDescriptor, completionHandler: (CLKComplicationWidgetMigrationConfiguration?) -> Void)](clkcomplicationwidgetmigrator/getwidgetconfiguration(from:completionhandler:).md)
  Returns a configuration object that defines the WidgetKit replacement for the provided ClockKit complication.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var widgetMigrator: any CLKComplicationWidgetMigrator](clkcomplicationdatasource/widgetmigrator.md)
  A migrator that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationStaticWidgetMigrationConfiguration](clkcomplicationstaticwidgetmigrationconfiguration.md)
  A configuration object that specifies a static complication in WidgetKit.
- [class CLKComplicationAppIntentWidgetMigrationConfiguration](clkcomplicationappintentwidgetmigrationconfiguration.md)
  A configuration object that specifies a WidgetKit complication that uses app intents.
- [class CLKComplicationIntentWidgetMigrationConfiguration](clkcomplicationintentwidgetmigrationconfiguration.md)
  A configuration object that specifies an intents-based complication in WidgetKit.
- [class CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
  An abstract class that specifies WidgetKit complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationwidgetmigrator)*