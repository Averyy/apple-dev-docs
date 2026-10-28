# contentRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle describing the content area of the tab view.

**Availability**:
- macOS

## Declaration

```swift
var contentRect: NSRect { get }
```

```objc
@property (readonly) NSRect contentRect;
```

## Discussion

This area does not include the space required for the tab view’s tabs or borders (if any).

## See Also

### Determining the Size
- [var minimumSize: NSSize](./minimumsize.md)
  The minimum size necessary for the tab view to display tabs in a useful way.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/contentrect)*