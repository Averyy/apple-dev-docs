# OpenSettingsAction

**Framework**: SwiftUI  
**Kind**: struct

An action that presents the settings scene for an app.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency struct OpenSettingsAction
```

#### Overview

Use the [`openSettings`](environmentvalues/opensettings.md) environment value to get the instance of this structure for a given [`Environment`](environment.md). Then call the instance to open a window. You call the instance directly because it defines a [`callAsFunction()`](opensettingsaction/callasfunction().md) method that Swift calls when you call the instance.

For example, you can define a button that opens the settings window to a particular tab:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Settings {
            SettingsView()
        }
        #endif
    }
}

struct SettingsView: View {
    @AppStorage("selectedSettingsTab")
    private var selectedSettingsTab = SettingsTab.general

    var body: some View {
        TabView(selection: $selectedSettingsTab) {
            GeneralSettings()
            AdvancedSettings()
        }
    }
}

struct AdvancedSettingsButton: View {
    @AppStorage("selectedSettingsTab")
    private var selectedSettingsTab = SettingsTab.general

    @Environment(\.openSettings) private var openSettings

    var body: some View {
        Button("Open Advanced Settings…") {
            selectedSettingsTab = .advanced
            openSettings()
        }
    }
}

enum SettingsTab: Int {
    case general
    case advanced
}
```

## Topics

### Instance Methods
- [func callAsFunction()](opensettingsaction/callasfunction.md)
  Opens the window associated to the [`Settings`](settings.md) scene defined by this app, if one exists.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Settings](settings.md)
  A scene that presents an interface for viewing and modifying an app’s settings.
- [struct SettingsLink](settingslink.md)
  A view that opens the Settings scene defined by an app.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/opensettingsaction)*