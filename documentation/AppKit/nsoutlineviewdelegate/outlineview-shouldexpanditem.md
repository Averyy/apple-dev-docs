# outlineView(_:shouldExpandItem:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the outline view should expand a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldExpandItem item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to permit `outlineView` to expand `item`, [`false`](https://developer.apple.com/documentation/Swift/false) to deny permission.

#### Discussion

The delegate can implement this method to disallow expanding of specific items.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item that should expand.

## See Also

- [Outline View](outline-view.md)
  Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one.
- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [func outlineView(NSOutlineView, shouldCollapseItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldcollapseitem:).md)
  Returns a Boolean value that indicates whether the outline view should collapse a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldexpanditem:))*