# widgetMigrator

**Framework**: ClockKit  
**Kind**: property

A migrator that maps ClockKit complications to their WidgetKit replacements.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
@MainActor
optional var widgetMigrator: any CLKComplicationWidgetMigrator { get }
```

#### Discussion

Implement this to provide an instance that can migrate a user’s ClockKit complications to their WidgetKit replacements. For example, update your data source so that it also conforms to the [`CLKComplicationWidgetMigrator`](clkcomplicationwidgetmigrator.md) protocol.

```swift
class ComplicationController: NSObject, CLKComplicationDataSource, CLKComplicationWidgetMigrator {
   // ...
}
```

Then, have its [`widgetMigrator`](clkcomplicationdatasource/widgetmigrator.md) property return `self`.

```swift
var widgetMigrator: CLKComplicationWidgetMigrator {
    self
}
```

Finally, implement the [`getWidgetConfiguration(from:completionHandler:)`](clkcomplicationwidgetmigrator/getwidgetconfiguration(from:completionhandler:).md) method. This method determines the best WidgetKit configuration for the given complication descriptor. The following example uses the Swift async version of the method.

```swift
func widgetConfiguration(from complicationDescriptor: CLKComplicationDescriptor) async -> CLKComplicationWidgetMigrationConfiguration? {
    
    switch complicationDescriptor.identifier {
    case caffeineDoseIdentifier:
        return CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "Caffeine_Complications",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")


    case cupTotalIdentifier:
        return CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "CupTotal_Complications",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")


    case cupAndCaffeineIdentifier:
        return CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "CupAndCaffeine_Complications",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")


    default:
        return nil
    }
}
```

## See Also

- [class CLKComplicationStaticWidgetMigrationConfiguration](clkcomplicationstaticwidgetmigrationconfiguration.md)
  A configuration object that specifies a static complication in WidgetKit.
- [class CLKComplicationAppIntentWidgetMigrationConfiguration](clkcomplicationappintentwidgetmigrationconfiguration.md)
  A configuration object that specifies a WidgetKit complication that uses app intents.
- [class CLKComplicationIntentWidgetMigrationConfiguration](clkcomplicationintentwidgetmigrationconfiguration.md)
  A configuration object that specifies an intents-based complication in WidgetKit.
- [protocol CLKComplicationWidgetMigrator](clkcomplicationwidgetmigrator.md)
  A protocol that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationWidgetMigrationConfiguration](clkcomplicationwidgetmigrationconfiguration.md)
  An abstract class that specifies WidgetKit complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/widgetmigrator)*