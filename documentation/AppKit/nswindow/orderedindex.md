# orderedIndex

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The zero-based position of the window, based on its order from front to back among all visible application windows.

**Availability**:
- macOS

## Declaration

```swift
var orderedIndex: Int { get set }
```

```objc
@property NSInteger orderedIndex;
```

## Discussion

If you set this property to an index that’s out of range, the system sets the position to the nearest value that’s in range.

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
- [var isResizable: Bool](./isresizable.md)
  A Boolean value that indicates if the user can resize the window.
- [var isMiniaturizable: Bool](./isminiaturizable.md)
  A Boolean value that indicates whether the window can minimize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderedindex)*