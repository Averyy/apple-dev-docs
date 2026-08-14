# CLKComplicationIntentWidgetMigrationConfiguration

**Framework**: ClockKit  
**Kind**: class

A configuration object that specifies an intents-based complication in WidgetKit.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
class CLKComplicationIntentWidgetMigrationConfiguration
```

#### Overview

These configuration objects use an [`INIntent`](https://developer.apple.com/documentation/intents/inintent) object to provide dynamic configuration information. Use intent-based complications when your app customizes the list of complications available in the complication picker based on the state of your app. For example, if you provide temperature complications for the top cities in the user’s favorites list, use an [`INIntent`](https://developer.apple.com/documentation/intents/inintent) object to describe each city.

For more information, see [`Migrating ClockKit complications to WidgetKit`](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app).

## Topics

### Creating Intent widget configurations
- [init(kind: String, extensionBundleIdentifier: String, intent: INIntent, localizedDisplayName: String)](clkcomplicationintentwidgetmigrationconfiguration/init(kind:extensionbundleidentifier:intent:localizeddisplayname:).md)
  Creates an object that describes an intents-based watchOS complication in your WidgetKit extension.
### Accessing configuration properties
- [var kind: String](clkcomplicationintentwidgetmigrationconfiguration/kind.md)
  A string that uniquely identifies a widget in your WidgetKit extension.
- [var extensionBundleIdentifier: String](clkcomplicationintentwidgetmigrationconfiguration/extensionbundleidentifier.md)
  The bundle identifier for your WidgetKit extension.
- [var intent: INIntent](clkcomplicationintentwidgetmigrationconfiguration/intent.md)
  A SiriKit intent that provides additional configuration information to your WidgetKit complication.
- [var localizedDisplayName: String](clkcomplicationintentwidgetmigrationconfiguration/localizeddisplayname.md)
  A localized name for the complication.

## Relationships

### Inherits From
- [CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var widgetMigrator: any CLKComplicationWidgetMigrator](clkcomplicationdatasource/widgetmigrator.md)
  A migrator that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationStaticWidgetMigrationConfiguration](clkcomplicationstaticwidgetmigrationconfiguration.md)
  A configuration object that specifies a static complication in WidgetKit.
- [class CLKComplicationAppIntentWidgetMigrationConfiguration](clkcomplicationappintentwidgetmigrationconfiguration.md)
  A configuration object that specifies a WidgetKit complication that uses app intents.
- [protocol CLKComplicationWidgetMigrator](clkcomplicationwidgetmigrator.md)
  A protocol that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
  An abstract class that specifies WidgetKit complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationintentwidgetmigrationconfiguration)*