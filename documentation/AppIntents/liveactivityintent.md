# LiveActivityIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
protocol LiveActivityIntent : SystemIntent
```

#### Overview

To gain permission for starting Live Activities, conform to this protocol. In general, your app needs to be in the foreground to start a Live Activity. However, you can use a `LiveActivityIntent` and start the Live Activity in its [`perform()`](appintent/perform().md) method. When the system performs the intent, the system launches your app process without opening the app, performs the intent, and starts the Live Activity. For example, people might place a control in Control Center that performs a `LiveActivityIntent` and starts the activity without opening your app. For more information about app intents, refer to [`App Intents`](AppIntents.md) and [`Making actions and content discoverable and widely available`](Making-actions-and-content-discoverable-and-widely-available.md).

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/liveactivityintent)*