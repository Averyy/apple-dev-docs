# enumerateDraggingItems(options:for:classes:searchOptions:using:)

**Framework**: AppKit  
**Kind**: method

Enumerates through each dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func enumerateDraggingItems(options enumOpts: NSDraggingItemEnumerationOptions = [], for view: NSView?, classes classArray: [AnyClass], searchOptions: [NSPasteboard.ReadingOptionKey : Any] = [:], using block: (NSDraggingItem, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

Enumerate through dragging items to modify their properties, such as the drag image or size, while the user is dragging. When the dragging items are over the destination, changes that the destination’s [`NSDraggingInfo`](nsdragginginfo.md) methods make may override changes you make during the drag session.

To get dragging items in a data type that you expect while enumerating, specify classes in the `classesArray` parameter that implement the [`NSPasteboardReading`](nspasteboardreading.md) protocol, such as `NSImage`, `NSString`, `NSURL`, `NSColor`, `NSAttributedString`, or `NSPasteboardItem`. For each item in the dragging pasteboard, the system performs the following steps:

1. The systems calls [`readableTypes(for:)`](nspasteboardreading/readabletypes(for:).md) on the item to determine the types of data the item conforms to.
2. It attempts to create an instance of a matching class from the dragging pasteboard data, using the class order you specify in the `classesArray` parameter.
3. If it can create an instance of a matching class, the system creates an instance of [`NSDraggingItem`](nsdraggingitem.md) with the class instance and the dragging properties of that item.
4. The system passes the `NSDraggingItem` to the block you provide as the `draggingItem` parameter.

If the system can’t create an instance of one of the classes you specify in `classesArray` with an item, the system skips the item without calling `block` and proceeds to the next item.

> 💡 **Tip**:  Ensure you receive one object per item on the pasteboard by including the [`NSPasteboardItem`](nspasteboarditem.md) class in the array of classes.

When the system provides a `draggingItem` to your block, modify the item’s properties to change how the user sees the item while dragging. Provide a `view` to this method if you want to express each dragging item’s `draggingFrame` relative to that `view`.

> ⚠️ **Warning**:  The `draggingItem` object is only valid for the current iteration of the enumeration block. Never store the `draggingItem` or change it outside of the block iteration. Don’t reference `draggingItem` inside an [`imageComponentsProvider`](nsdraggingitem/imagecomponentsprovider.md) block for the following reasons: ・When the system calls the `imageComponentsProvider` block, the enumeration block is out of scope and the `draggingItem` is no longer valid. ・Referencing `draggingItem` in an `imageComponentsProvider` block creates a retain cycle because `draggingItem` retains `imageComponentsProvider`, and `imageComponentsProvider` retains `draggingItem`. Assign `draggingItem.item` to an object pointer or variable outside of the `imageComponentsProvider` block definition instead, and use that object pointer or variable inside the [`imageComponentsProvider`](nsdraggingitem/imagecomponentsprovider.md) block definition.

To refine the list of dragging items that this method provides, specify `enumOpts` and `searchOptions`.

## Parameters

- `enumOpts`: The enumeration options. See [`NSDraggingItemEnumerationOptions`](nsdraggingitemenumerationoptions.md) for the supported values.
- `view`: The view to use as the base coordinate system for the [`NSDraggingItem`](nsdraggingitem.md) instances.
- `classArray`: An array of class objects. Arrange classes in the array in the preferred order of representation. Classes in the array must conform to the [`NSPasteboardReading`](nspasteboardreading.md) protocol.
- `searchOptions`: A dictionary that specifies options to refine the search for pasteboard items, such as restricting the search to file URLs with particular content types. For valid dictionary keys, see [`NSPasteboard.ReadingOptionKey`](nspasteboard/readingoptionkey.md).
- `block`: The block to execute for the enumeration. The block takes three arguments: - **`draggingItem`**: A reference to the dragging item. The [`draggingFrame`](nsdraggingitem/draggingframe.md) of the dragging item is in the coordinate space of the view that `view` specifies. A `view` value of `nil` means the screen coordinate space.
- **`idx`**: The index of the element in the classes.
- **`stop`**: A reference to a Boolean value that the block can use to stop the enumeration by setting `*stop` to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsession/enumeratedraggingitems(options:for:classes:searchoptions:using:))*