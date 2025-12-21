# outlineView(_:shouldCollapseItem:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the outline view should collapse a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldCollapseItem item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to permit `outlineView` to collapse `item`, [`false`](https://developer.apple.com/documentation/Swift/false) to deny permission.

#### Discussion

The delegate can implement this method to disallow collapsing of specific items. For example, if the first row of your outline view should not be collapsed, your delegate method could contain this line of code:

```objc
return [outlineView rowForItem:item]!=0;
```

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item that should collapse.

## See Also

- [func outlineView(NSOutlineView, shouldExpandItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldexpanditem:).md)
  Returns a Boolean value that indicates whether the outline view should expand a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldcollapseitem:))*