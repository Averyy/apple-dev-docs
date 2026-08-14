# RunSystemShortcutIntent

**Framework**: App Intents  
**Kind**: struct

An app intent you use in widgets to open another app or perform an App Shortcut, custom shortcut, or system action.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct RunSystemShortcutIntent
```

#### Overview

Only use `RunSystemShortcutIntent` to initialize a [`Button`](https://developer.apple.com/documentation/swiftui/button) with the [`init(_:intent:)`](https://developer.apple.com/documentation/swiftui/button/init(_:intent:)) initializer and place the button in a widget. The run system shortcut intent doesn’t provide functionality in other contexts.

When a person configures the widget, they choose the button’s action. It can:

- Open another installed app.
- Perform an App Shortcut.
- Perform a custom shortcut a person creates in Shortcuts.
- Perform a system action.

The following example shows how an app offers a widget that allows people to launch another app from a button:

```swift
import SwiftUI
import WidgetKit
import AppIntents

struct LauncherWidgetConfigurationIntent: WidgetConfigurationIntent {
    static var title: LocalizedStringResource { "Launcher Widget" }
    static var description: IntentDescription { "Widget that runs a shortcut or opens an app" }

    @Parameter(title: "Action")
    var shortcut: SystemShortcut
}

struct LauncherWidget: Widget {
    let kind: String = "LauncherWidget"

    var body: some WidgetConfiguration {
        AppIntentConfiguration(
            kind: kind,
            intent: LauncherWidgetConfigurationIntent.self,
            provider: Provider()
        ) { entry in
            Button(
                intent: RunSystemShortcutIntent(shortcut: entry.configuration.shortcut)
            ) {
                VStack {
                    Image(systemName: "play.fill")
                        .font(.largeTitle)
                    Text(entry.configuration.shortcut.displayRepresentation.title)
                        .font(.caption)
                }
            }
        }
    }
}
```

The `RunSystemShortcutIntent` represents a person’s chosen action when they configure your widget and it provides metadata the system needs for the widget’s configuration UI. It doesn’t provide your widget or app with access to a shortcut’s actions, parameters, or implementation details. If a custom shortcut or App Shortcut requires an interaction, for example, if it prompts a person for input, the system may open the Shortcuts app to perform the intent.

## Topics

### Creating the intent
- [init(shortcut: SystemShortcut)](runsystemshortcutintent/init(shortcut:).md)
  Creates an intent that performs a person’s configured action.
- [struct SystemShortcut](systemshortcut.md)
  An opaque reference to a user-configured action for use in a widget button.
### Initializers
- [init()](runsystemshortcutintent/init.md)
  Creates an intent that performs a person’s configured action.
### Instance Methods
- [func perform() async throws -> IntentResultContainer<Never, Never, Never, Never>](runsystemshortcutintent/perform.md)
  Performs a widget’s configured action, like opening another app or performing an App Shortcut, custom shortcut, or system action.
### Type Properties
- [static let persistentIdentifier: String](runsystemshortcutintent/persistentidentifier.md)
  The string that identifies the intent.
- [static let title: LocalizedStringResource](runsystemshortcutintent/title.md)
  The localized string that describes the intent’s functionality.

## Relationships

### Conforms To
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/runsystemshortcutintent)*