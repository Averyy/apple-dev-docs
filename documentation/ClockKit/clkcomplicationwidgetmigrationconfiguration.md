# CLKComplicationWidgetMigrationConfiguration

**Framework**: ClockKit  
**Kind**: class

An abstract class that specifies WidgetKit complications.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
class CLKComplicationWidgetMigrationConfiguration
```

#### Overview

The [`CLKComplicationWidgetMigrationConfiguration`](clkcomplicationwidgetmigrationconfiguration.md) class is the basis for all classes that describe watchOS complications in WidgetKit. Because it’s an abstract class, you don’t instantiate it directly. Instead, create one of its concrete subclasses: [`CLKComplicationStaticWidgetMigrationConfiguration`](clkcomplicationstaticwidgetmigrationconfiguration.md), [`CLKComplicationAppIntentWidgetMigrationConfiguration`](clkcomplicationappintentwidgetmigrationconfiguration.md), or [`CLKComplicationIntentWidgetMigrationConfiguration`](clkcomplicationintentwidgetmigrationconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CLKComplicationAppIntentWidgetMigrationConfiguration](clkcomplicationappintentwidgetmigrationconfiguration.md)
- [CLKComplicationIntentWidgetMigrationConfiguration](clkcomplicationintentwidgetmigrationconfiguration.md)
- [CLKComplicationStaticWidgetMigrationConfiguration](clkcomplicationstaticwidgetmigrationconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [protocol CLKComplicationWidgetMigrator](clkcomplicationwidgetmigrator.md)
  A protocol that maps ClockKit complications to their WidgetKit replacements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationwidgetmigrationconfiguration)*