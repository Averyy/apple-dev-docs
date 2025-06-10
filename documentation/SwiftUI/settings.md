# Settings

**Framework**: SwiftUI  
**Kind**: struct

A scene that presents an interface for viewing and modifying an app’s settings.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct Settings<Content> where Content : View
```

## Mentions

- [Declaring a custom view](declaring-a-custom-view.md)
- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)

#### Overview

Use a settings scene to have SwiftUI manage views with controls for your app’s settings when you declare your app using the [`App`](app.md) protocol. When you use an [`App`](app.md) declaration for multiple platforms, compile the settings scene only in macOS:

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
```

Passing a view as the argument to a settings scene in the [`App`](app.md) declaration causes SwiftUI to enable the app’s Settings menu item. SwiftUI manages displaying and removing the settings view when the user selects the Settings item from the application menu or the equivalent keyboard shortcut:

![A screenshot of the MyApp application menu, showing the active](https://docs-assets.developer.apple.com/published/6816987b7f2629737c2e5427ab99ad8d/SwiftUI-AppBehavior-Settings-AppMenu%402x.png)

The contents of your settings view are controls that modify bindings to [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) values that SwiftUI manages using the [`AppStorage`](appstorage.md) property wrapper:

```swift
struct GeneralSettingsView: View {
    @AppStorage("showPreview") private var showPreview = true
    @AppStorage("fontSize") private var fontSize = 12.0

    var body: some View {
        Form {
            Toggle("Show Previews", isOn: $showPreview)
            Slider(value: $fontSize, in: 9...96) {
                Text("Font Size (\(fontSize, specifier: "%.0f") pts)")
            }
        }
    }
}
```

You can define your settings in a single view, or you can use a [`TabView`](tabview.md) to group settings into different collections:

```swift
struct SettingsView: View {
    var body: some View {
        TabView {
            Tab("General", systemImage: "gear") {
                GeneralSettingsView()
            }
            Tab("Advanced", systemImage: "star") {
                AdvancedSettingsView()
            }
        }
        .scenePadding()
        .frame(maxWidth: 350, minHeight: 100)
    }
}
```

![A screenshot showing a tabbed application settings view containing a](https://docs-assets.developer.apple.com/published/01f778a442e362d593a8937912132520/SwiftUI-AppBehavior-Settings%402x.png)

## Topics

### Creating a settings scene
- [init(content: () -> Content)](settings/init(content:).md)
  Creates a scene that presents an interface for viewing and modifying an app’s preferences.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [struct SettingsLink](settingslink.md)
  A view that opens the Settings scene defined by an app.
- [struct OpenSettingsAction](opensettingsaction.md)
  An action that presents the settings scene for an app.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/settings)*