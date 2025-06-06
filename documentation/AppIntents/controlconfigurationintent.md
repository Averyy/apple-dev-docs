# ControlConfigurationIntent

**Framework**: App Intents  
**Kind**: protocol

An interface for configuring a Control Center module.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
protocol ControlConfigurationIntent : AppIntent
```

#### Overview

The parameters of your intent define all of the configuration options for your control.

```swift
struct SelectFocusIntent: ControlConfigurationIntent {
    static let title: LocalizedStringResource = "Select Focus"
    static let description: IntentDescription = "Turn Focus on to silence notifications and filter out distractions."

    struct FocusOptionsProvider: DynamicOptionsProvider {
        func results() async throws -> [Focus] {
            FocusManager.shared.allFocuses
        }
    }

    @Parameter(title: "Focus", default: .doNotDisturb, optionsProvider: FocusOptionsProvider())
    var focus: Focus
}
```

When using this protocol, you don’t need to provide an implementation for [`perform()`](appintent/perform().md). You can, however, still implement `perform()` to use the same implementation for both control configuration and as an actionable intent.

The example above provides a default value for the `focus` intent parameter. By providing a default value, you can use a non-optional value for the intent parameter. If you don’t provide a default value for the intent parameter, the parameter’s value must be optional, to allow the system to preview the control before someone configures it.

## Topics

### Associated Types
- [associatedtype NeverResult](controlconfigurationintent/neverresult.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/controlconfigurationintent)*