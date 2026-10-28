# outlineViewItemDidCollapse(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the did collapse notification is posted—that is, whenever the user collapses an item in the outline view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func outlineViewItemDidCollapse(_ notification: Notification)
```

```objc
- (void) outlineViewItemDidCollapse:(NSNotification *) notification;
```

## Discussion

This method is invoked as a result of posting an [`itemDidCollapseNotification`](../nsoutlineview/itemdidcollapsenotification.md).

## Parameters

- `notification`: The posted notification.

## See Also

### Working with the Outline Column
- [func outlineViewColumnDidMove(Notification)](./outlineviewcolumndidmove%28_%29.md)
  Invoked whenever the user moves a column in the outline view.
- [func outlineViewColumnDidResize(Notification)](./outlineviewcolumndidresize%28_%29.md)
  Invoked whenever the user resizes a column in the outline view.
- [func outlineViewItemWillExpand(Notification)](./outlineviewitemwillexpand%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the user is about to expand an item in the outline view.
- [func outlineViewItemDidExpand(Notification)](./outlineviewitemdidexpand%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the user expands an item in the outline view.
- [func outlineViewItemWillCollapse(Notification)](./outlineviewitemwillcollapse%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the user is about to collapse an item in the outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineviewitemdidcollapse(_:))*