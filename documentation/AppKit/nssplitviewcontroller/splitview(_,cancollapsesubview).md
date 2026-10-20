# splitView(_:canCollapseSubview:)

**Framework**: AppKit  
**Kind**: method

Allows the split view controller to determine whether the user can collapse and expand the specified subview.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, canCollapseSubview subview: NSView) -> Bool
```

## See Also

- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](nssplitviewcontroller/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:).md)
  Allows the split view controller to determine if a subview collapses in response to a double click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:cancollapsesubview:))*