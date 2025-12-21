# outlineView(_:isGroupItem:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean that indicates whether a given row should be drawn in the “group row” style.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, isGroupItem item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to indicate a particular row should have the “group row” style drawn for that row, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the cell in that row is an instance of `NSTextFieldCell` and contains only a string value, the “group row” style attributes are automatically applied for that cell.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: An item in the outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:isgroupitem:))*