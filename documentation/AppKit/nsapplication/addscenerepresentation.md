# addSceneRepresentation(_:)

**Framework**: AppKit  
**Kind**: method

Adds the specified SwiftUI scene representation to the current application.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func addSceneRepresentation<C>(_ representation: NSHostingSceneRepresentation<C>) where C : Scene
```

#### Discussion

Scenes defined by the representation can be presented programmatically via the environment actions available on `NSHostingSceneRepresentation`, or when the app receives an external event such as a URL.

For example, you can add a `Settings` scene to your app and present it when the corresponding menu item is selected:

```None
import AppKit
import SwiftUI

@main
class ApplicationDelegate: NSApplicationDelegate {
    let scene = NSHostingSceneRepresentation {
        Settings {
            SettingsView()
        }
    }

    func applicationWillFinishLaunching(
        _ notification: Notification
    ) {
        NSApplication.shared.addSceneRepresentation(scene)
    }

    @IBAction func showAppSettings(_ sender: NSMenuItem) {
        scene.openSettings()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/addscenerepresentation(_:))*