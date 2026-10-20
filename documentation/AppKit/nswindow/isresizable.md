# isResizable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the user can resize the window.

**Availability**:
- macOS

## Declaration

```swift
var isResizable: Bool { get }
```

```objc
@property (readonly, getter=isResizable) BOOL resizable;
```

#### Discussion

This property is key-value coding compliant.

## See Also

### Getting Information About Scripting Attributes
- [var hasCloseBox: Bool](./hasclosebox.md)
  A Boolean value that indicates if the window has a close box.
- [var hasTitleBar: Bool](./hastitlebar.md)
  A Boolean value that indicates if the window has a title bar.
- [var isModalPanel: Bool](./ismodalpanel.md)
  A Boolean value that indicates whether the window is a modal panel.
- [var isFloatingPanel: Bool](./isfloatingpanel.md)
  A Boolean value that indicates whether the window is a floating panel.
- [var isZoomable: Bool](./iszoomable.md)
  A Boolean value that indicates whether the window allows zooming.
- [var isMiniaturizable: Bool](./isminiaturizable.md)
  A Boolean value that indicates whether the window can minimize.
- [var orderedIndex: Int](./orderedindex.md)
  The zero-based position of the window, based on its order from front to back among all visible application windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isresizable)*