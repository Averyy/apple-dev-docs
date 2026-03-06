# defaultSize(_:in:)

**Framework**: SwiftUI  
**Kind**: method

Sets a default size for a volumetric window.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func defaultSize(_ size: Size3D, in unit: UnitLength) -> some Scene
```

#### Return Value

A scene that uses a default size for new windows.

#### Discussion

Use this modifier to indicate the default initial size for a new 3D window created from a [`Scene`](scene.md) using [`VolumetricWindowStyle`](volumetricwindowstyle.md):

```swift
WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
.defaultSize(Size3D(width: 1, height: 1, depth: 0.5), in: .meters)
```

Each parameter is specified in the unit you provide. The size of a volumetric scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## Parameters

- `unit`: The unit of length the dimensions of the window are specified in.

## See Also

- [Positioning and sizing windows](../visionOS/positioning-and-sizing-windows.md)
  Influence the initial geometry of windows that your app presents.
- [func defaultSize(_:)](scene/defaultsize(_:).md)
  Sets a default size for a window.
- [func defaultSize(width: CGFloat, height: CGFloat) -> some Scene](scene/defaultsize(width:height:).md)
  Sets a default width and height for a window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some Scene](scene/defaultsize(width:height:depth:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/defaultsize(_:in:))*