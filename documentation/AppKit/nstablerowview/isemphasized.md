# isEmphasized

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the row will draw with the alternate or secondary color (unless overridden).

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isEmphasized: Bool { get set }
```

```objc
@property (getter=isEmphasized) BOOL emphasized;
```

## Discussion

When emphasized is [`true`](../../Swift/true.md), the view will draw with the [`alternateSelectedControlColor`](../nscolor/alternateselectedcontrolcolor.md) defined by [`NSColor`](../nscolor.md). When [`false`](../../Swift/false.md) it will use the [`secondarySelectedControlColor`](../nscolor/secondaryselectedcontrolcolor.md) defined by [`NSColor`](../nscolor.md).

## See Also

### Related Documentation
- [Table View](../table-view.md)
  Display custom data in rows and columns.
- [Drag and Drop](../drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
### Display Style
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./interiorbackgroundstyle.md)
  Specifies how the subviews should draw.
- [var isFloating: Bool](./isfloating.md)
  Specifies whether the row is drawn using the floating style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/isemphasized)*