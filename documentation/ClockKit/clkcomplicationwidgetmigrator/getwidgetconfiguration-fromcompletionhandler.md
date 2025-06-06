# getWidgetConfiguration(from:completionHandler:)

**Framework**: ClockKit  
**Kind**: method

Returns a configuration object that defines the WidgetKit replacement for the provided ClockKit complication.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
optional func widgetConfiguration(from complicationDescriptor: CLKComplicationDescriptor) async -> CLKComplicationWidgetMigrationConfiguration?
```

#### Discussion

Implement this method to provide the best WidgetKit configuration for the given complication descriptor. Your implementation examines the complication descriptor, then creates a configuration object and passes it to the completion handler.

```swift
func getWidgetConfiguration(from complicationDescriptor: CLKComplicationDescriptor, completionHandler: @escaping (CLKComplicationWidgetMigrationConfiguration?) -> Void) {
    
    var configuration: CLKComplicationWidgetMigrationConfiguration? = nil
    
    switch complicationDescriptor.identifier {
    case caffeineDoseIdentifier:
        configuration = CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "Caffeine_Complications",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")
        
    case cupTotalIdentifier:
        configuration = CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "CupTotal_Complications",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")
        
    case cupAndCaffeineIdentifier:
        configuration = CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "CupAndCaffeine_Complications",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")
        
    default:
        configuration = nil
    }
    
    completionHandler(configuration)
    
}
```

> ❗ **Important**:  After you add a WidgetKit extension to your project, the system tries to use it to generate complications for your watchOS app. As soon as your WidgetKit extension begins providing widget-based complications, the system disables your app’s ClockKit complications. It no longer wakes your app to call your [`CLKComplicationDataSource`](clkcomplicationdatasource.md) object’s methods to request timeline entries. However, the system may still wake your data source to call [`getWidgetConfiguration(from:completionHandler:)`](clkcomplicationwidgetmigrator/getwidgetconfiguration(from:completionhandler:).md) while migrating complications from ClockKit to WidgetKit.

 After you add a WidgetKit extension to your project, the system tries to use it to generate complications for your watchOS app. As soon as your WidgetKit extension begins providing widget-based complications, the system disables your app’s ClockKit complications. It no longer wakes your app to call your [`CLKComplicationDataSource`](clkcomplicationdatasource.md) object’s methods to request timeline entries. However, the system may still wake your data source to call [`getWidgetConfiguration(from:completionHandler:)`](clkcomplicationwidgetmigrator/getwidgetconfiguration(from:completionhandler:).md) while migrating complications from ClockKit to WidgetKit.

For more information, see [`Migrating ClockKit complications to WidgetKit`](https://developer.apple.com/documentation/WidgetKit/Converting-A-ClockKit-App).

## Parameters

- `complicationDescriptor`: A descriptor that identifies a ClockKit complication.
- `completionHandler`: A completion handler that your implementation calls after you create a configuration object that defines the WidgetKit replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationwidgetmigrator/getwidgetconfiguration(from:completionhandler:))*