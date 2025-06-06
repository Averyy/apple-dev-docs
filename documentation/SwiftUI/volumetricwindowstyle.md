# VolumetricWindowStyle

**Framework**: SwiftUI  
**Kind**: struct

A window style that creates a 3D volumetric window.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct VolumetricWindowStyle
```

#### Overview

Use [`volumetric`](windowstyle/volumetric.md) to construct this style:

```swift
WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
```

## Topics

### Creating the window style
- [init()](volumetricwindowstyle/init.md)

## Relationships

### Conforms To
- [WindowStyle](windowstyle.md)

## See Also

- [struct DefaultWindowStyle](defaultwindowstyle.md)
  The default window style.
- [struct HiddenTitleBarWindowStyle](hiddentitlebarwindowstyle.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [struct PlainWindowStyle](plainwindowstyle.md)
  The plain window style.
- [struct TitleBarWindowStyle](titlebarwindowstyle.md)
  A window style which displays the title bar section of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/volumetricwindowstyle)*