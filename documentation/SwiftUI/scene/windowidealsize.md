# windowIdealSize(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies how windows derived form this scene should determine their size when zooming.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowIdealSize(_ idealSize: WindowIdealSize) -> some Scene
```

#### Discussion

The default behavior will size the window to its maximum size, or the bounds of the display, whichever is smaller. By overriding this behavior, you can provide a size that is appropriate for the contents of your window.

For example, you can define a window group where the window has an ideal width of 800 points and an ideal height of 600 points:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(idealWidth: 800, idealHeight: 600)
        }
        .windowIdealSize(.fitToContent)
    }
}
```

## Parameters

- `idealSize`: A value which determines how windows derived from   this scene should size themselves when zooming.

## See Also

- [Positioning and sizing windows](../visionOS/positioning-and-sizing-windows.md)
  Influence the initial geometry of windows that your app presents.
- [func defaultSize(_:)](scene/defaultsize(_:).md)
  Sets a default size for a window.
- [func defaultSize(width: CGFloat, height: CGFloat) -> some Scene](scene/defaultsize(width:height:).md)
  Sets a default width and height for a window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some Scene](scene/defaultsize(width:height:depth:).md)
  Sets a default size for a volumetric window.
- [func defaultSize(Size3D, in: UnitLength) -> some Scene](scene/defaultsize(_:in:).md)
  Sets a default size for a volumetric window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in: UnitLength) -> some Scene](scene/defaultsize(width:height:depth:in:).md)
  Sets a default size for a volumetric window.
- [func windowResizability(WindowResizability) -> some Scene](scene/windowresizability(_:).md)
  Sets the kind of resizability to use for a window.
- [struct WindowResizability](windowresizability.md)
  The resizability of a window.
- [struct WindowIdealSize](windowidealsize.md)
  A type which defines the size a window should use when zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowidealsize(_:))*