# WindowIdealSize

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type which defines the size a window should use when zooming.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct WindowIdealSize
```

#### Overview

Use this type in conjunction with the `Scene.windowIdealSize(_:)` modifier to override the default behavior for how windows behave when performing a zoom.

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

## Topics

### Type Properties
- [static let automatic: WindowIdealSize](./windowidealsize/automatic.md)
  The automatic window ideal size. Windows will use the system behavior when determining the size to use when zooming.
- [static let fitToContent: WindowIdealSize](./windowidealsize/fittocontent.md)
  A window ideal size which uses the ideal size of the window’s contents.
- [static let maximum: WindowIdealSize](./windowidealsize/maximum.md)
  A window ideal size which uses the maximum size of the window’s contents.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sizing a window
- [Positioning and sizing windows](../visionOS/positioning-and-sizing-windows.md)
  Influence the initial geometry of windows that your app presents.
- [func defaultSize(_:)](./scene/defaultsize%28_%29.md)
  Sets a default size for a window.
- [func defaultSize(width: CGFloat, height: CGFloat) -> some Scene](./scene/defaultsize%28width,height%29.md)
  Sets a default width and height for a window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some Scene](./scene/defaultsize%28width,height,depth%29.md)
  Sets a default size for a volumetric window.
- [func defaultSize(Size3D, in: UnitLength) -> some Scene](./scene/defaultsize%28_,in%29.md)
  Sets a default size for a volumetric window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in: UnitLength) -> some Scene](./scene/defaultsize%28width,height,depth,in%29.md)
  Sets a default size for a volumetric window.
- [func windowResizability(WindowResizability) -> some Scene](./scene/windowresizability%28_%29.md)
  Sets the kind of resizability to use for a window.
- [struct WindowResizability](./windowresizability.md)
  The resizability of a window.
- [func windowIdealSize(WindowIdealSize) -> some Scene](./scene/windowidealsize%28_%29.md)
  Specifies how windows derived form this scene should determine their size when zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowidealsize)*