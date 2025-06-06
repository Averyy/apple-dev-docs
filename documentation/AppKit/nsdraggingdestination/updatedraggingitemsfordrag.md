# updateDraggingItemsForDrag(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when the dragging images should be changed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func updateDraggingItemsForDrag(_ sender: (any NSDraggingInfo)?)
```

#### Discussion

While a destination may change the dragging images at any time, it is recommended to wait until this method is called before updating the dragging images.

This allows the system to delay changing the dragging images until it is likely that the user will drop on this destination. Otherwise, the dragging images will change too often during the drag which would be distracting to the user.

During `enumerateDraggingItemsWithOptions:forView:classes:searchOptions:usingBlock:` you may set non-acceptable drag items images to `nil` to hide them or use the enumeration option of [`clearNonenumeratedImages`](nsdraggingitemenumerationoptions/clearnonenumeratedimages.md)  If there are items that you hide, then after enumeration, you need to set the [`numberOfValidItemsForDrop`](nsdragginginfo/numberofvaliditemsfordrop.md) to the number of non-hidden drag items. However, if the valid item count is `0`, then it is better to return [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md) from your implementation of [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md) and, or [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) instead of hiding all drag items during enumeration.

## Parameters

- `sender`: The object sending the message; use this object to get details about the dragging operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/updatedraggingitemsfordrag(_:))*