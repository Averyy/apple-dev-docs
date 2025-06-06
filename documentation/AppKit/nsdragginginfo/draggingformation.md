# draggingFormation

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The formation of the dragging items while the drag is over the destination.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var draggingFormation: NSDraggingFormation { get set }
```

#### Discussion

Set this property to change the formation of the drag items. This is generally done during the [`updateDraggingItemsForDrag(_:)`](nsdraggingdestination/updatedraggingitemsfordrag(_:).md) method or whenever you enumerate the dragging items.

The default value is the current drag formation.

> **Note**:  Set this property before or after the [`NSDraggingInfo`](nsdragginginfo.md) or [`NSDraggingSession`](nsdraggingsession.md) class’s method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdragginginfo/enumeratedraggingitems(options:for:classes:searchoptions:using:).md) not inside the enumeration Block.

 Set this property before or after the [`NSDraggingInfo`](nsdragginginfo.md) or [`NSDraggingSession`](nsdraggingsession.md) class’s method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdragginginfo/enumeratedraggingitems(options:for:classes:searchoptions:using:).md) not inside the enumeration Block.

## See Also

- [func slideDraggedImage(to: NSPoint)](nsdragginginfo/slidedraggedimage(to:).md)
  Slides the image to a specified location.
- [var animatesToDestination: Bool](nsdragginginfo/animatestodestination.md)
  A Boolean value that indicates whether the dragging formation animates while the drag is over the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggingformation)*