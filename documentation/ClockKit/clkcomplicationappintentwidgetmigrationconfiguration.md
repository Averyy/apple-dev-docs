# CLKComplicationAppIntentWidgetMigrationConfiguration

**Framework**: ClockKit  
**Kind**: class

A configuration object that specifies a WidgetKit complication that uses app intents.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
class CLKComplicationAppIntentWidgetMigrationConfiguration<Intent> where Intent : WidgetConfigurationIntent
```

#### Overview

These configuration objects use app intents to provide dynamic configuration information. Use intent-based complications when your app customizes the list of complications available in the complication picker based on the state of your app. For example, if you provide temperature complications for the top cities in the user’s favorites list, use a [`WidgetConfigurationIntent`](https://developer.apple.com/documentation/AppIntents/WidgetConfigurationIntent) instance to describe each city.

For more information, see [`Migrating ClockKit complications to WidgetKit`](https://developer.apple.com/documentation/WidgetKit/Converting-A-ClockKit-App).

## Topics

### Creating configurations
- [init(kind: String, extensionBundleIdentifier: String, intent: Intent, localizedDisplayName: String)](clkcomplicationappintentwidgetmigrationconfiguration/init(kind:extensionbundleidentifier:intent:localizeddisplayname:).md)
  Creates an object that describes a watchOS complication that uses app intents in your WidgetKit extension.
### Accessing configuration properties
- [let kind: String](clkcomplicationappintentwidgetmigrationconfiguration/kind.md)
  A string that uniquely identifies a widget in your WidgetKit extension.
- [let extensionBundleIdentifier: String](clkcomplicationappintentwidgetmigrationconfiguration/extensionbundleidentifier.md)
  The bundle identifier for your WidgetKit extension.
- [let intent: Intent](clkcomplicationappintentwidgetmigrationconfiguration/intent.md)
  An intent that provides additional configuration information to your WidgetKit complication.
- [let localizedDisplayName: String](clkcomplicationappintentwidgetmigrationconfiguration/localizeddisplayname.md)
  A localized name for the complication.
### Initializers
- [init?(coder: NSCoder)](clkcomplicationappintentwidgetmigrationconfiguration/init(coder:).md)

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
- [class CLKComplicationStaticWidgetMigrationConfiguration](clkcomplicationstaticwidgetmigrationconfiguration.md)
  A configuration object that specifies a static complication in WidgetKit.
- [class CLKComplicationIntentWidgetMigrationConfiguration](clkcomplicationintentwidgetmigrationconfiguration.md)
  A configuration object that specifies an intents-based complication in WidgetKit.
- [protocol CLKComplicationWidgetMigrator](clkcomplicationwidgetmigrator.md)
  A protocol that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
  An abstract class that specifies WidgetKit complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationappintentwidgetmigrationconfiguration)*