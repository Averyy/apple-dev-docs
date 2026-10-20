# splitView(_:canCollapseSubview:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the split view controller to determine whether the user can collapse and expand the specified subview.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, canCollapseSubview subview: NSView) -> Bool
```

```objc
- (BOOL) splitView:(NSSplitView *) splitView canCollapseSubview:(NSView *) subview;
```

## See Also

### Managing Subviews
- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](./splitview%28_,shouldcollapsesubview,fordoubleclickondividerat%29.md)
  Allows the split view controller to determine if a subview collapses in response to a double click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:cancollapsesubview:))*