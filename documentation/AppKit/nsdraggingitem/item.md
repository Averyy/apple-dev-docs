# item

**Framework**: AppKit  
**Kind**: property

The pasteboard reader or writer object dependent on the context where you use the dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var item: Any { get }
```

#### Discussion

When you create an `NSDraggingItem` instance, `item` is the `pasteboardWriter` passed to [`init(pasteboardWriter:)`](nsdraggingitem/init(pasteboardwriter:).md).

However, when enumerating dragging items using the [`NSDraggingSession`](nsdraggingsession.md) method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdraggingsession/enumeratedraggingitems(options:for:classes:searchoptions:using:).md) or the [`NSDraggingInfo`](nsdragginginfo.md) method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdragginginfo/enumeratedraggingitems(options:for:classes:searchoptions:using:).md), `item` is not the original pasteboard reader or writer instance. It is an instance of one of the classes provided to the enumeration method’s `classArray` parameter.

## See Also

- [var imageComponents: [NSDraggingImageComponent]?](nsdraggingitem/imagecomponents.md)
  An array of dragging image components to use to create the drag image.
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](nsdraggingitem/imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [NSDraggingItem.ImageComponentKey](nsdraggingitem/imagecomponentkey.md)
  Keys that identify components of a dragging image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/item)*