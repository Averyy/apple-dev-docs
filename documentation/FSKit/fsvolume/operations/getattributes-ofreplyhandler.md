# getAttributes(_:of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Fetches attributes for the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func attributes(_ desiredAttributes: FSItem.GetAttributesRequest, of item: FSItem) async throws -> FSItem.Attributes
```

#### Discussion

For file systems that don’t support hard links, set [`linkCount`](fsitem/attributes/linkcount.md) to `1` for regular files and symbolic links.

If the item’s `bsdFlags` contain the `UF_COMPRESSED` flag, your file system returns the uncompressed size of the file.

## Parameters

- `desiredAttributes`: A requested set of attributes to get. The implementation inspects the request’s   to determine which attributes to populate.
- `item`: The item to get attributes for.
- `reply`: A block or closure to indicate success or failure. If getting attributes succeeds, pass an   with the requested attributes populated and a   error. If getting attributes fails, pass the relevant error as the second parameter; FSKit ignores any   in this case. For an   Swift implementation, there’s no reply handler; simply return the   or throw an error.

## See Also

- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, replyHandler: (FSItem.Attributes?, (any Error)?) -> Void)](fsvolume/operations/setattributes(_:on:replyhandler:).md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/getattributes(_:of:replyhandler:))*