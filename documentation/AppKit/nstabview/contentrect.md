# contentRect

**Framework**: AppKit  
**Kind**: property

The rectangle describing the content area of the tab view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentRect: NSRect { get }
```

#### Discussion

This area does not include the space required for the tab view’s tabs or borders (if any).

## See Also

- [var minimumSize: NSSize](nstabview/minimumsize.md)
  The minimum size necessary for the tab view to display tabs in a useful way.
- [var controlSize: NSControl.ControlSize](nstabview/controlsize.md)
  The size of the tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/contentrect)*