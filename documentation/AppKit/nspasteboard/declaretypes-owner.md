# declareTypes(_:owner:)

**Framework**: Appkit  
**Kind**: method

Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.

**Availability**:
- macOS ?+

## Declaration

```swift
func declareTypes(_ newTypes: [NSPasteboard.PasteboardType], owner newOwner: Any?) -> Int
```

#### Return Value

The receiver’s new change count.

#### Discussion

This method is the equivalent of invoking [`clearContents()`](nspasteboard/clearcontents().md), implicitly writing the first pasteboard item, and then calling [`addTypes(_:owner:)`](nspasteboard/addtypes(_:owner:).md) to promise types for the first pasteboard item.

> **Note**:  In macOS 10.5 and earlier, this method is the first step in writing data to the pasteboard and must precede the messages that actually write the data. A [`declareTypes(_:owner:)`](nspasteboard/declaretypes(_:owner:).md) message essentially changes the contents of the receiver: It invalidates the current contents of the receiver and increments its change count.

##### Special Considerations

In general, you should not use this method with [`writeObjects(_:)`](nspasteboard/writeobjects(_:).md), since [`writeObjects(_:)`](nspasteboard/writeobjects(_:).md) will always write additional items to the pasteboard, and will not affect items already on the pasteboard, including the item implicitly created by this method.

## Parameters

- `newTypes`: An array of   objects that specify the types of data that may be added to the new pasteboard. The types should be ordered according to the preference of the source application, with the most preferred type coming first (typically, the richest representation).
- `newOwner`: The object responsible for writing data to the pasteboard, or   if you provide data for all types immediately. If you specify a   object, it must support all of the types declared in the   parameter and must remain alive for as long as the data is   on the pasteboard.

## See Also

- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [var changeCount: Int](nspasteboard/changecount.md)
  The receiver’s change count.
- [func addTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/addtypes(_:owner:).md)
  Adds promises for the specified types to the first pasteboard item.
- [func writeFileContents(String) -> Bool](nspasteboard/writefilecontents(_:).md)
  Writes the contents of the specified file to the pasteboard.
- [func write(FileWrapper) -> Bool](nspasteboard/write(_:).md)
  Writes the serialized contents of the specified file wrapper to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/declaretypes(_:owner:))*