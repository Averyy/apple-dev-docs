# windowResizability(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the kind of resizability to use for a window.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func windowResizability(_ resizability: WindowResizability) -> some Scene
```

#### Return Value

A scene that uses the specified resizability strategy.

#### Discussion

Use this scene modifier to apply a value of type [`WindowResizability`](windowresizability.md) to a [`Scene`](scene.md) that you define in your [`App`](app.md) declaration. The value that you specify indicates the strategy the system uses to place minimum and maximum size restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between 100 and 400 points in both dimensions by applying both a frame with those constraints to the scene’s content, and the [`contentSize`](windowresizability/contentsize.md) resizability to the scene:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(
                    minWidth: 100, maxWidth: 400,
                    minHeight: 100, maxHeight: 400)
        }
        .windowResizability(.contentSize)
    }
}
```

The default value for all scenes if you don’t apply the modifier is [`automatic`](windowresizability/automatic.md). With that strategy, [`Settings`](settings.md) windows use the [`contentSize`](windowresizability/contentsize.md) strategy, while all others use [`contentMinSize`](windowresizability/contentminsize.md).

## Parameters

- `resizability`: The resizability to use for windows created by   this scene.

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
- [struct WindowResizability](windowresizability.md)
  The resizability of a window.
- [func windowIdealSize(WindowIdealSize) -> some Scene](scene/windowidealsize(_:).md)
  Specifies how windows derived form this scene should determine their size when zooming.
- [struct WindowIdealSize](windowidealsize.md)
  A type which defines the size a window should use when zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowresizability(_:))*