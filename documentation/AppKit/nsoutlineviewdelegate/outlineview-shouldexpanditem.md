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

- [Outline View Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OutlineView/OutlineView.html#//apple_ref/doc/uid/10000023i)
- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [func outlineView(NSOutlineView, shouldCollapseItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldcollapseitem:).md)
  Returns a Boolean value that indicates whether the outline view should collapse a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldexpanditem:))*