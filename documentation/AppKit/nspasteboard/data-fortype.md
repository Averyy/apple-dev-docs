# data(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the data for the specified type from the first item in the receiver that contains the type.

**Availability**:
- macOS ?+

## Declaration

```swift
func data(forType dataType: NSPasteboard.PasteboardType) -> Data?
```

#### Return Value

A data object containing the data for the specified type from the first item in the receiver that contains the type, or `nil` if the contents of the pasteboard changed since they were last checked.

#### Discussion

This method may also return `nil` if the pasteboard server cannot supply the data in time—for example, if the pasteboard’s owner is slow in responding to a [`pasteboard:provideDataForType:`](https://developer.apple.com/documentation/objectivec/nsobject/1525907-pasteboard) message and the interprocess communication times out.

#### Discussion

Errors other than a timeout raise an `NSPasteboardCommunicationException`.

If `nil` is returned, the application should put up a panel informing the user that it was unable to carry out the paste operation. Note that sending [`types`](nspasteboard/types.md) or [`availableType(from:)`](nspasteboard/availabletype(from:).md) before invoking [`data(forType:)`](nspasteboard/data(fortype:).md) can help you determine whether a `nil` result from a reading method is due to something like a pasteboard timeout.

##### Special Considerations

For standard text data types such as string, RTF, and RTFD, the text data from each item is returned as one combined result separated by newlines.

## Parameters

- `dataType`: The type of data you want to read from the pasteboard. This value should be one of the types returned by   or  .

## See Also

- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey.md)
  Options for reading pasteboard data.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](nspasteboard/pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func index(of: NSPasteboardItem) -> Int](nspasteboard/index(of:).md)
  Returns the index of the specified pasteboard item.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboard/propertylist(fortype:).md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboard/string(fortype:).md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/data(fortype:))*