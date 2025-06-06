# isEmphasized

**Framework**: AppKit  
**Kind**: property

Determines whether the row will draw with the alternate or secondary color (unless overridden).

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var isEmphasized: Bool { get set }
```

#### Discussion

When emphasized is [`true`](https://developer.apple.com/documentation/swift/true), the view will draw with the [`alternateSelectedControlColor`](nscolor/alternateselectedcontrolcolor.md) defined by [`NSColor`](nscolor.md). When [`false`](https://developer.apple.com/documentation/swift/false) it will use the [`secondarySelectedControlColor`](nscolor/secondaryselectedcontrolcolor.md) defined by [`NSColor`](nscolor.md).

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nstablerowview/interiorbackgroundstyle.md)
  Specifies how the subviews should draw.
- [var isFloating: Bool](nstablerowview/isfloating.md)
  Specifies whether the row is drawn using the floating style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/isemphasized)*