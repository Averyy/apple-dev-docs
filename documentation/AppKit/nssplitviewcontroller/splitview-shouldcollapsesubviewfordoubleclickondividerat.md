# splitView(_:shouldCollapseSubview:forDoubleClickOnDividerAt:)

**Framework**: AppKit  
**Kind**: method

Allows the split view controller to determine if a subview collapses in response to a double click.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, shouldCollapseSubview subview: NSView, forDoubleClickOnDividerAt dividerIndex: Int) -> Bool
```

## See Also

- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](nssplitviewcontroller/splitview(_:cancollapsesubview:).md)
  Allows the split view controller to determine whether the user can collapse and expand the specified subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:))*