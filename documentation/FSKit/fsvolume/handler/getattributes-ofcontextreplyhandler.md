# getAttributes(_:of:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Fetches attributes for the given item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func attributes(_ desiredAttributes: FSItem.GetAttributesRequest, of item: FSItem, context: FSContext) async throws -> FSGetAttributesResult
```

#### Discussion

For file systems that don’t support hard links, set [`linkCount`](fsitem/attributes/linkcount.md) to `1` for regular files and symbolic links.

If the item’s `bsdFlags` contain the `UF_COMPRESSED` flag, your file system returns the uncompressed size of the file.

## Parameters

- `desiredAttributes`: A requested set of attributes to get. The implementation inspects the request’s [`wantedAttributes`](fsitem/getattributesrequest/wantedattributes.md) to determine which attributes to populate.
- `item`: The item to get attributes for.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If getting attributes succeeds, pass an instance of [`FSGetAttributesResult`](fsgetattributesresult.md) containing the requested attributes, along with a `nil` error. If getting attributes fails, pass the relevant error as the second parameter; FSKit ignores the [`FSGetAttributesResult`](fsgetattributesresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [class FSGetAttributesResult](fsgetattributesresult.md)
  The result of a get-attributes call.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, context: FSContext, replyHandler: (FSSetAttributesResult?, (any Error)?) -> Void)](fsvolume/handler/setattributes(_:on:context:replyhandler:).md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSSetAttributesResult](fssetattributesresult.md)
  The restlt of a set-attributes call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/getattributes(_:of:context:replyhandler:))*