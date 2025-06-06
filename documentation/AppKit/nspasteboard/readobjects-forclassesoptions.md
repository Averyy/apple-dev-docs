# readObjects(forClasses:options:)

**Framework**: AppKit  
**Kind**: method

Reads from the receiver objects that best match the specified array of classes.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func readObjects(forClasses classArray: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]? = nil) -> [Any]?
```

#### Return Value

An array containing the best match (if any) for each of the items on the receiver that can be represented by a class specified in `classArray`. Returns `nil` if there is an error in retrieving the requested items from the pasteboard, or an empty array if no objects of the specified classes can be created.

#### Discussion

Classes in `classArray` must implement the `NSPasteboardReading` protocol. Cocoa classes that implement this protocol include `NSImage`, `NSString`, `NSURL`, `NSColor`, `NSAttributedString`, and `NSPasteboardItem`.  For every item on the pasteboard, each class in the provided array will be queried for the types it can read using [`readableTypes(for:)`](nspasteboardreading/readabletypes(for:).md).  An instance is created of the first class found in the provided array whose readable types match a conforming type contained in that pasteboard item. Any instances that could be created from pasteboard item data is returned to the caller.  Additional options, such as restricting the search to file URLs with particular content types, can be specified with an options dictionary.

Only objects of the requested classes are returned. You can always ensure to receive one object per item on the pasteboard by including the [`NSPasteboardItem`](nspasteboarditem.md) class in the array of classes.

Consider the following example: there are five items on the pasteboard, two contain TIFF data, two contain RTF data, one contains a private data type. The following table shows what objects you get back in the returned array for different classes in `classArray`.

| Classes in `classArray` | Returned objects |
| --- | --- |
| `NSImage` | Two `NSImage` objects. |
| `NSAttributedString` | Two `NSAttributedString` objects. |
| `NSImage`, `NSAttributedString` | Two `NSImage` objects, and two `NSAttributedString` objects. |
| `NSImage`, `NSAttributedString`, `NSPasteboardItem` | Two `NSImage` objects, two `NSAttributedString` objects, and one `NSPasteboardItem` object containing the private data type. |

## Parameters

- `classArray`: Because this method creates an instance of the first class that can read a given pasteboard item, you can order the classes in   to match your preferred order of representation. Classes in the array must conform to the   protocol.
- `options`: A dictionary that specifies options to refine the search for pasteboard items, for example to restrict the search to file URLs with particular content types. For valid dictionary keys, see  .

## See Also

- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](nspasteboard/canreaditem(withdataconformingtotypes:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](nspasteboard/canreadobject(forclasses:options:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey.md)
  Options for reading pasteboard data.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](nspasteboard/pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func index(of: NSPasteboardItem) -> Int](nspasteboard/index(of:).md)
  Returns the index of the specified pasteboard item.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboard/data(fortype:).md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboard/propertylist(fortype:).md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboard/string(fortype:).md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readobjects(forclasses:options:))*