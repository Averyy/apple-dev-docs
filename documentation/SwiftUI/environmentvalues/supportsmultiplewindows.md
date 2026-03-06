# supportsMultipleWindows

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether the current platform supports opening multiple windows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var supportsMultipleWindows: Bool { get }
```

#### Discussion

Read this property from the environment to determine if your app can use the [`openWindow`](environmentvalues/openwindow.md) action to open new windows:

```swift
struct NewMailViewerButton: View {
    @Environment(\.supportsMultipleWindows) private var supportsMultipleWindows
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open New Window") {
            openWindow(id: "mail-viewer")
        }
        .disabled(!supportsMultipleWindows)
    }
}
```

The reported value depends on both the platform and how you configure your app:

- In macOS, this property returns `true` for any app that uses the SwiftUI app lifecycle.
- In iPadOS, this property returns `true` for any app that uses the SwiftUI app lifecycle and has the Information Property List key [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) set to `true`.
- For all other platforms and configurations, the value returns `false`.

If the value is false and you try to open a window, SwiftUI ignores the action and logs a runtime error.

## See Also

- [Presenting windows and spaces](../visionOS/presenting-windows-and-spaces.md)
  Open and close the scenes that make up your app’s interface.
- [var openWindow: OpenWindowAction](environmentvalues/openwindow.md)
  A window presentation action stored in a view’s environment.
- [struct OpenWindowAction](openwindowaction.md)
  An action that presents a window.
- [struct PushWindowAction](pushwindowaction.md)
  An action that opens the requested window in place of the window the action is called from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/supportsmultiplewindows)*