# CLKComplicationStaticWidgetMigrationConfiguration

**Framework**: ClockKit  
**Kind**: class

A configuration object that specifies a static complication in WidgetKit.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
class CLKComplicationStaticWidgetMigrationConfiguration
```

#### Overview

You can use static complications if your app doesn’t dynamically customize the list of complications available in the complication picker. For example, if your complications display the current temperature and chance of precipitation at the user’s current location, you can use a set of static widgets to define these complications.

For more information, see [`Migrating ClockKit complications to WidgetKit`](https://developer.apple.com/documentation/WidgetKit/Converting-A-ClockKit-App).

## Topics

### Creating static complication configurations
- [init(kind: String, extensionBundleIdentifier: String)](clkcomplicationstaticwidgetmigrationconfiguration/init(kind:extensionbundleidentifier:).md)
  Creates an object that describes a static watchOS complication in your WidgetKit extension.
### Accessing configuration properties
- [var kind: String](clkcomplicationstaticwidgetmigrationconfiguration/kind.md)
  A string that uniquely identifies a widget in your WidgetKit extension.
- [var extensionBundleIdentifier: String](clkcomplicationstaticwidgetmigrationconfiguration/extensionbundleidentifier.md)
  The bundle identifier for your WidgetKit extension.

## Relationships

### Inherits From
- [CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
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
- [class CLKComplicationAppIntentWidgetMigrationConfiguration](clkcomplicationappintentwidgetmigrationconfiguration.md)
  A configuration object that specifies a WidgetKit complication that uses app intents.
- [class CLKComplicationIntentWidgetMigrationConfiguration](clkcomplicationintentwidgetmigrationconfiguration.md)
  A configuration object that specifies an intents-based complication in WidgetKit.
- [protocol CLKComplicationWidgetMigrator](clkcomplicationwidgetmigrator.md)
  A protocol that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
  An abstract class that specifies WidgetKit complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationstaticwidgetmigrationconfiguration)*