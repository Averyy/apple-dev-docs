# outlineViewColumnDidResize(_:)

**Framework**: AppKit  
**Kind**: method

Invoked whenever the user resizes a column in the outline view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func outlineViewColumnDidResize(_ notification: Notification)
```

#### Discussion

This method is invoked as a result of posting an [`columnDidResizeNotification`](nsoutlineview/columndidresizenotification.md).

## Parameters

- `notification`: The posted notification.

## See Also

- [func outlineViewColumnDidMove(Notification)](nsoutlineviewdelegate/outlineviewcolumndidmove(_:).md)
  Invoked whenever the user moves a column in the outline view.
- [func outlineViewItemWillExpand(Notification)](nsoutlineviewdelegate/outlineviewitemwillexpand(_:).md)
  Invoked when `notification` is posted—that is, whenever the user is about to expand an item in the outline view.
- [func outlineViewItemDidExpand(Notification)](nsoutlineviewdelegate/outlineviewitemdidexpand(_:).md)
  Invoked when `notification` is posted—that is, whenever the user expands an item in the outline view.
- [func outlineViewItemWillCollapse(Notification)](nsoutlineviewdelegate/outlineviewitemwillcollapse(_:).md)
  Invoked when `notification` is posted—that is, whenever the user is about to collapse an item in the outline view.
- [func outlineViewItemDidCollapse(Notification)](nsoutlineviewdelegate/outlineviewitemdidcollapse(_:).md)
  Invoked when the did collapse notification is posted—that is, whenever the user collapses an item in the outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineviewcolumndidresize(_:))*