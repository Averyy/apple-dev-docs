# orderedIndex

**Framework**: AppKit  
**Kind**: property

The zero-based position of the window, based on its order from front to back among all visible application windows.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var orderedIndex: Int { get set }
```

#### Discussion

If you set this property to an index that’s out of range, the system sets the position to the nearest value that’s in range.

## See Also

- [var hasCloseBox: Bool](nswindow/hasclosebox.md)
  A Boolean value that indicates if the window has a close box.
- [var hasTitleBar: Bool](nswindow/hastitlebar.md)
  A Boolean value that indicates if the window has a title bar.
- [var isModalPanel: Bool](nswindow/ismodalpanel.md)
  A Boolean value that indicates whether the window is a modal panel.
- [var isFloatingPanel: Bool](nswindow/isfloatingpanel.md)
  A Boolean value that indicates whether the window is a floating panel.
- [var isZoomable: Bool](nswindow/iszoomable.md)
  A Boolean value that indicates whether the window allows zooming.
- [var isResizable: Bool](nswindow/isresizable.md)
  A Boolean value that indicates if the user can resize the window.
- [var isMiniaturizable: Bool](nswindow/isminiaturizable.md)
  A Boolean value that indicates whether the window can minimize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderedindex)*