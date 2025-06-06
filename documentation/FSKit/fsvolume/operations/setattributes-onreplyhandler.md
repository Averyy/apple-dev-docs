# setAttributes(_:on:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Sets the given attributes on an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func setAttributes(_ newAttributes: FSItem.SetAttributesRequest, on item: FSItem) async throws -> FSItem.Attributes
```

#### Discussion

Several attributes are considered “read-only”, and an attempt to set these attributes results in an error with the code `EINVAL`.

A request may set [`size`](fsitem/attributes/size.md) beyond the end of the file. If the underlying file system doesn’t support sparse files, allocate space to fill the new file size. Either fill this space with zeroes, or configure it to read as zeroes.

If a request sets the file size below the current end-of-file, truncate the file and return any unused space to the file system as free space.

Ignore attempts to set the size of directories or symbolic links; don’t produce an error.

If the caller attepts to sest an attribute not supported by the on-disk file system format, don’t produce an error. The upper layers of the framework will detect this situation.

## Parameters

- `newAttributes`: A request containing the attributes to set.
- `item`: The item on which to set the attributes.
- `reply`: A block or closure to indicate success or failure. If setting attributes succeeds, pass an   with the item’s updated attributes and a   error. If setting attributes fails, pass the relevant error as the second parameter; FSKit ignores any   in this case. For an   Swift implementation, there’s no reply handler; simply return the   or throw an error.

## See Also

- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, replyHandler: (FSItem.Attributes?, (any Error)?) -> Void)](fsvolume/operations/getattributes(_:of:replyhandler:).md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/setattributes(_:on:replyhandler:))*