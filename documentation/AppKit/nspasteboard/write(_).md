# write(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the serialized contents of the specified file wrapper to the pasteboard.

**Availability**:
- macOS

## Declaration

```swift
func write(_ wrapper: FileWrapper) -> Bool
```

```objc
- (BOOL) writeFileWrapper:(NSFileWrapper *) wrapper;
```

## Return Value

[`true`](../../Swift/true.md) if the data was successfully written, otherwise [`false`](../../Swift/false.md).

## Discussion

Writes the serialized contents of the file wrapper `wrapper` to the receiver and declares the data to be of type `NSFileContentsPboardType` and also of a type appropriate for the file’s extension (as returned by the `NSCreateFileContentsPboardType` function when passed the files extension), if it has one. If `wrapper` does not have a preferred filename, this method raises an exception.

## Parameters

- `wrapper`: The file wrapper to write to the pasteboard.

## See Also

### Writing data (macOS 10.5 and earlier)
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](./declaretypes%28_,owner%29.md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func addTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](./addtypes%28_,owner%29.md)
  Adds promises for the specified types to the first pasteboard item.
- [func writeFileContents(String) -> Bool](./writefilecontents%28_%29.md)
  Writes the contents of the specified file to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/write(_:))*