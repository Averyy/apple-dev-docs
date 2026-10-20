# splitView(_:shouldCollapseSubview:forDoubleClickOnDividerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the split view controller to determine if a subview collapses in response to a double click.

**Availability**:
- macOS 10.5+ - Deprecated in 10.15

> **Deprecated**: [`NSSplitView`](../nssplitview.md) no longer supports collapsing sections using a double click. The system never calls this delegate method, and this implementation always returns [`false`](../../Swift/false.md).

## Declaration

```swift
func splitView(_ splitView: NSSplitView, shouldCollapseSubview subview: NSView, forDoubleClickOnDividerAt dividerIndex: Int) -> Bool
```

```objc
- (BOOL) splitView:(NSSplitView *) splitView shouldCollapseSubview:(NSView *) subview forDoubleClickOnDividerAtIndex:(NSInteger) dividerIndex;
```

## See Also

### Managing Subviews
- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](./splitview%28_,cancollapsesubview%29.md)
  Allows the split view controller to determine whether the user can collapse and expand the specified subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:))*