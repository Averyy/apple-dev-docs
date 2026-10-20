# plain

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The plain window style.

**Availability**:
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var plain: PlainWindowStyle { get }
```

Available when `Self` is `PlainWindowStyle`.

#### Discussion

Unlike [`automatic`](./automatic.md), a plain window does not receive a glass background in visionOS or window chrome in macOS. Use this style if you want more control over how these elements are used in your window.

## See Also

### Getting built-in window styles
- [static var automatic: DefaultWindowStyle](./automatic.md)
  The default window style.
- [static var hiddenTitleBar: HiddenTitleBarWindowStyle](./hiddentitlebar.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [static var titleBar: TitleBarWindowStyle](./titlebar.md)
  A window style which displays the title bar section of the window.
- [static var volumetric: VolumetricWindowStyle](./volumetric.md)
  A window style that creates a 3D volumetric window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowstyle/plain)*