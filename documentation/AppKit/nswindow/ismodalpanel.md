# isModalPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is a modal panel.

**Availability**:
- macOS

## Declaration

```swift
var isModalPanel: Bool { get }
```

```objc
@property (readonly, getter=isModalPanel) BOOL modalPanel;
```

#### Discussion

This property is key-value coding compliant.

## See Also

### Getting Information About Scripting Attributes
- [var hasCloseBox: Bool](./hasclosebox.md)
  A Boolean value that indicates if the window has a close box.
- [var hasTitleBar: Bool](./hastitlebar.md)
  A Boolean value that indicates if the window has a title bar.
- [var isFloatingPanel: Bool](./isfloatingpanel.md)
  A Boolean value that indicates whether the window is a floating panel.
- [var isZoomable: Bool](./iszoomable.md)
  A Boolean value that indicates whether the window allows zooming.
- [var isResizable: Bool](./isresizable.md)
  A Boolean value that indicates if the user can resize the window.
- [var isMiniaturizable: Bool](./isminiaturizable.md)
  A Boolean value that indicates whether the window can minimize.
- [var orderedIndex: Int](./orderedindex.md)
  The zero-based position of the window, based on its order from front to back among all visible application windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismodalpanel)*