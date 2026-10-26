# intentWidgetMigrationConfigurationWithKind:extensionBundleIdentifier:intent:localizedDisplayName:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Creates an object that describes an intents-based watchOS complication in your WidgetKit extension.

**Availability**:
- watchOS 9.0+

## Declaration

```objc
+ (instancetype) intentWidgetMigrationConfigurationWithKind:(NSString *) kind extensionBundleIdentifier:(NSString *) extensionBundleIdentifier intent:(INIntent *) intent localizedDisplayName:(NSString *) localizedDisplayName;
```

## Parameters

- `kind`: A string that uniquely identifies a widget in your WidgetKit extension.
- `extensionBundleIdentifier`: The bundle identifier for your WidgetKit extension.
- `intent`: A SiriKit intent that provides additional configuration information to your WidgetKit complication.
- `localizedDisplayName`: A localized name for the complication.

## See Also

### Creating Intent widget configurations
- [init(kind: String, extensionBundleIdentifier: String, intent: INIntent, localizedDisplayName: String)](./init%28kind,extensionbundleidentifier,intent,localizeddisplayname%29.md)
  Creates an object that describes an intents-based watchOS complication in your WidgetKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationintentwidgetmigrationconfiguration/intentwidgetmigrationconfigurationwithkind:extensionbundleidentifier:intent:localizeddisplayname:)*