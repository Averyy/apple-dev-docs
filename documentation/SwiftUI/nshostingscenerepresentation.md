# NSHostingSceneRepresentation

**Framework**: SwiftUI  
**Kind**: class

An AppKit type that hosts and can present SwiftUI scenes

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class NSHostingSceneRepresentation<Content> where Content : Scene
```

#### Overview

Use instances of this type with `NSApplication.addSceneRepresentation(_:)` to include SwiftUI scene functionality in an app which uses the AppKit app lifecycle.

For example, you can add a `Settings` scene to your app and present it when the corresponding menu item is selected:

```swift
import AppKit
import SwiftUI

@main
class ApplicationDelegate: NSApplicationDelegate {
    let settingsScene = NSHostingSceneRepresentation {
        Settings {
            SettingsView()
        }
    }

    func applicationWillFinishLaunching(_ notification: Notification) {
        NSApplication.shared.addSceneRepresentation(settingsScene)
    }

    @IBAction func showAppSettings(_ sender: NSMenuItem) {
        settingsScene.environment.openSettings()
    }
}
```

## Topics

### Initializers
- [init(rootScene: () -> Content)](nshostingscenerepresentation/init(rootscene:).md)
  Creates a new hosting scene representation for the specified scene(s).
### Instance Properties
- [var environment: EnvironmentValues](nshostingscenerepresentation/environment.md)
  The environment for any scene(s) being represented by `self`.

## See Also

- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingView](nshostingview.md)
  An AppKit view that hosts a SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [struct NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingscenerepresentation)*