# outlineView(_:shouldCollapseItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the outline view should collapse a given item.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldCollapseItem item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldCollapseItem:(id) item;
```

## Return Value

[`true`](../../Swift/true.md) to permit `outlineView` to collapse `item`, [`false`](../../Swift/false.md) to deny permission.

## Discussion

The delegate can implement this method to disallow collapsing of specific items. For example, if the first row of your outline view should not be collapsed, your delegate method could contain this line of code:

```objc
return [outlineView rowForItem:item]!=0;
```

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item that should collapse.

## See Also

### Expanding and Collapsing the Outline
- [func outlineView(NSOutlineView, shouldExpandItem: Any) -> Bool](./outlineview%28_,shouldexpanditem%29.md)
  Returns a Boolean value that indicates whether the outline view should expand a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldcollapseitem:))*