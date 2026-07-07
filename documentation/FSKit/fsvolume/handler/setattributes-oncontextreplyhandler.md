# setAttributes(_:on:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Sets the given attributes on an item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func setAttributes(_ newAttributes: FSItem.SetAttributesRequest, on item: FSItem, context: FSContext) async throws -> FSSetAttributesResult
```

#### Discussion

Several attributes are considered “read-only”, and an attempt to set these attributes results in an error with the code `EINVAL`.

A request may set [`size`](fsitem/attributes/size.md) beyond the end of the file. If the underlying file system doesn’t support sparse files, allocate space to fill the new file size. Either fill this space with zeroes, or configure it to read as zeroes.

If a request sets the file size below the current end-of-file, truncate the file and return any unused space to the file system as free space.

Ignore attempts to set the size of directories or symbolic links; don’t produce an error.

If the caller attempts to set an attribute not supported by the on-disk file system format, don’t produce an error. The upper layers of the framework will detect this situation.

## Parameters

- `newAttributes`: A request containing the attributes to set.
- `item`: The item on which to set the attributes.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If setting attributes succeeds, pass an instance of [`FSSetAttributesResult`](fssetattributesresult.md) containing the item’s updated attributes and the volume’s updated free space, along with a `nil` error. If setting attributes fails, pass the relevant error as the second parameter; FSKit ignores the [`FSSetAttributesResult`](fssetattributesresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, context: FSContext, replyHandler: (FSGetAttributesResult?, (any Error)?) -> Void)](fsvolume/handler/getattributes(_:of:context:replyhandler:).md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [class FSGetAttributesResult](fsgetattributesresult.md)
  The result of a get-attributes call.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSSetAttributesResult](fssetattributesresult.md)
  The restlt of a set-attributes call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/setattributes(_:on:context:replyhandler:))*