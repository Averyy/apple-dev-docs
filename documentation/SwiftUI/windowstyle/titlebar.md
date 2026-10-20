# titleBar

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A window style which displays the title bar section of the window.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@export(implementation)
static var titleBar: TitleBarWindowStyle { get }
```

Available when `Self` is `TitleBarWindowStyle`.

## See Also

### Getting built-in window styles
- [static var automatic: DefaultWindowStyle](./automatic.md)
  The default window style.
- [static var hiddenTitleBar: HiddenTitleBarWindowStyle](./hiddentitlebar.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [static var plain: PlainWindowStyle](./plain.md)
  The plain window style.
- [static var volumetric: VolumetricWindowStyle](./volumetric.md)
  A window style that creates a 3D volumetric window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowstyle/titlebar)*