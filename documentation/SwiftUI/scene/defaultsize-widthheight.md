# defaultSize(width:height:)

**Framework**: SwiftUI  
**Kind**: method

Sets a default width and height for a window.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func defaultSize(width: CGFloat, height: CGFloat) -> some Scene
```

#### Return Value

A scene that uses a default size for new windows.

#### Discussion

Use this scene modifier to indicate a default initial size for a new window that the system creates from a [`Scene`](scene.md) declaration. For example, you can request that new windows that a [`WindowGroup`](windowgroup.md) generates occupy 600 points in the x-dimension and 400 points in the y-dimension:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultSize(width: 600, height: 400)
    }
}
```

The size that you specify acts only as a default for when the window first appears. People can later resize the window using interface controls that the system provides. Also, during state restoration, the system restores windows to their most recent size rather than the default size.

If you specify a default size that’s outside the range of the window’s inherent resizability in one or both dimensions, the system clamps the affected dimension to keep it in range. You can configure the resizability of a scene using the [`windowResizability(_:)`](scene/windowresizability(_:).md) modifier.

The default size modifier affects any scene type that creates windows in macOS, namely:

- [`WindowGroup`](windowgroup.md)
- [`Window`](window.md)
- [`DocumentGroup`](documentgroup.md)
- [`Settings`](settings.md)

If you want to specify the size input in terms of size instance, use [`defaultSize(_:)`](scene/defaultsize(_:).md) instead.

## Parameters

- `width`: The default width for windows created from a scene.
- `height`: The default height for windows created from a scene.

## See Also

- [Positioning and sizing windows](../visionOS/positioning-and-sizing-windows.md)
  Influence the initial geometry of windows that your app presents.
- [func defaultSize(_:)](scene/defaultsize(_:).md)
  Sets a default size for a window.
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
- [func windowIdealSize(WindowIdealSize) -> some Scene](scene/windowidealsize(_:).md)
  Specifies how windows derived form this scene should determine their size when zooming.
- [struct WindowIdealSize](windowidealsize.md)
  A type which defines the size a window should use when zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/defaultsize(width:height:))*