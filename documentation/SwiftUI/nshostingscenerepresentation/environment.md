# environment

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The environment for any scene(s) being represented by `self`.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var environment: EnvironmentValues { get }
```

#### Discussion

Use the environment values to programmatically present a scene’s window.

For example, you can present the window for a `Settings` scene using `OpenSettingsAction` when a menu item is selected:

```swift
let settingsScene = NSHostingSceneRepresentation {
    Settings {
        SettingsView()
    }
}

@IBAction func showAppSettings(_ sender: NSMenuItem) {
    settingsScene.environment.openSettings()
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingscenerepresentation/environment)*