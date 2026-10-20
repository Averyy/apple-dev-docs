# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default window style.

**Availability**:
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var automatic: DefaultWindowStyle { get }
```

Available when `Self` is `DefaultWindowStyle`.

## See Also

### Getting built-in window styles
- [static var hiddenTitleBar: HiddenTitleBarWindowStyle](./hiddentitlebar.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [static var plain: PlainWindowStyle](./plain.md)
  The plain window style.
- [static var titleBar: TitleBarWindowStyle](./titlebar.md)
  A window style which displays the title bar section of the window.
- [static var volumetric: VolumetricWindowStyle](./volumetric.md)
  A window style that creates a 3D volumetric window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowstyle/automatic)*