# init(kind:extensionBundleIdentifier:intent:localizedDisplayName:)

**Framework**: ClockKit  
**Kind**: init

Creates an object that describes an intents-based watchOS complication in your WidgetKit extension.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
init(kind: String, extensionBundleIdentifier: String, intent: INIntent, localizedDisplayName: String)
```

## Parameters

- `kind`: A string that uniquely identifies a widget in your WidgetKit extension.
- `extensionBundleIdentifier`: The bundle identifier for your WidgetKit extension.
- `intent`: A SiriKit intent that provides additional configuration information to your WidgetKit complication.
- `localizedDisplayName`: A localized name for the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationintentwidgetmigrationconfiguration/init(kind:extensionbundleidentifier:intent:localizeddisplayname:))*