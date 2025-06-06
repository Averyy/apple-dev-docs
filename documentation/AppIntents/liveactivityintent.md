# LiveActivityIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol LiveActivityIntent : SystemIntent
```

#### Overview

To gain permission for starting Live Activities, conform to this protocol. Create and start a Live Activity manually in your [`perform()`](appintent/perform().md) method. For more information, see the [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit) framework.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
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