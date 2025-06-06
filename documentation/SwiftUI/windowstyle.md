# WindowStyle

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance and interaction of a window.

**Availability**:
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol WindowStyle
```

## Topics

### Getting built-in window styles
- [static var automatic: DefaultWindowStyle](windowstyle/automatic.md)
  The default window style.
- [static var hiddenTitleBar: HiddenTitleBarWindowStyle](windowstyle/hiddentitlebar.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [static var plain: PlainWindowStyle](windowstyle/plain.md)
  The plain window style.
- [static var titleBar: TitleBarWindowStyle](windowstyle/titlebar.md)
  A window style which displays the title bar section of the window.
- [static var volumetric: VolumetricWindowStyle](windowstyle/volumetric.md)
  A window style that creates a 3D volumetric window.
### Supporting types
- [struct DefaultWindowStyle](defaultwindowstyle.md)
  The default window style.
- [struct HiddenTitleBarWindowStyle](hiddentitlebarwindowstyle.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [struct PlainWindowStyle](plainwindowstyle.md)
  The plain window style.
- [struct TitleBarWindowStyle](titlebarwindowstyle.md)
  A window style which displays the title bar section of the window.
- [struct VolumetricWindowStyle](volumetricwindowstyle.md)
  A window style that creates a 3D volumetric window.

## Relationships

### Conforming Types
- [DefaultWindowStyle](defaultwindowstyle.md)
- [HiddenTitleBarWindowStyle](hiddentitlebarwindowstyle.md)
- [PlainWindowStyle](plainwindowstyle.md)
- [TitleBarWindowStyle](titlebarwindowstyle.md)
- [VolumetricWindowStyle](volumetricwindowstyle.md)

## See Also

- [struct WindowGroup](windowgroup.md)
  A scene that presents a group of identically structured windows.
- [struct Window](window.md)
  A scene that presents its content in a single, unique window.
- [struct UtilityWindow](utilitywindow.md)
  A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [func windowStyle<S>(S) -> some Scene](scene/windowstyle(_:).md)
  Sets the style for windows created by this scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowstyle)*