# item

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The pasteboard reader or writer object dependent on the context where you use the dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var item: Any { get }
```

```objc
@property (strong, readonly) id item;
```

#### Discussion

When you create an `NSDraggingItem` instance, `item` is the `pasteboardWriter` passed to [`init(pasteboardWriter:)`](./init%28pasteboardwriter%29.md).

However, when enumerating dragging items using the [`NSDraggingSession`](../nsdraggingsession.md) method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](../nsdraggingsession/enumeratedraggingitems%28options,for,classes,searchoptions,using%29.md) or the [`NSDraggingInfo`](../nsdragginginfo.md) method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](../nsdragginginfo/enumeratedraggingitems%28options,for,classes,searchoptions,using%29.md), `item` is not the original pasteboard reader or writer instance. It is an instance of one of the classes provided to the enumeration method’s `classArray` parameter.

## See Also

### Drag image components
- [var imageComponents: [NSDraggingImageComponent]?](./imagecomponents.md)
  An array of dragging image components to use to create the drag image.
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](./imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [NSDraggingItem.ImageComponentKey](./imagecomponentkey.md)
  Keys that identify components of a dragging image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/item)*