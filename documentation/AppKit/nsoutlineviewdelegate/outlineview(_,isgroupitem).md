# outlineView(_:isGroupItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean that indicates whether a given row should be drawn in the “group row” style.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, isGroupItem item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView isGroupItem:(id) item;
```

#### Return Value

[`true`](../../Swift/true.md) to indicate a particular row should have the “group row” style drawn for that row, otherwise [`false`](../../Swift/false.md).

#### Discussion

If the cell in that row is an instance of `NSTextFieldCell` and contains only a string value, the “group row” style attributes are automatically applied for that cell.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: An item in the outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:isgroupitem:))*