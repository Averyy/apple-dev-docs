# createLink(to:named:in:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new hard link.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func createLink(to item: FSItem, named name: FSFileName, in directory: FSItem, context: FSContext) async throws -> FSCreateLinkResult
```

#### Discussion

If creating the link fails, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and the following error codes:

- `EEXIST` if there’s already an item named `name` in the directory.
- `EMLINK` if creating the link would exceed the maximum number of hard links supported on `item`.
- `ENOTSUP` if the file system doesn’t support creating hard links to the type of file system object that `item` represents.

## Parameters

- `item`: The existing item to which to link.
- `name`: The name for the new link.
- `directory`: The directory in which to create the link.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass an instance of [`FSCreateLinkResult`](fscreatelinkresult.md) containing the [`FSFileName`](fsfilename.md) of the newly-created link, the [`FSItem.Attributes`](fsitem/attributes.md) of the linked item, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory, and the volume’s updated free space, along with a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCreateLinkResult`](fscreatelinkresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSCreateLinkResult](fscreatelinkresult.md)
  The result of a create-link call.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:).md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/readsymboliclink(_:context:replyhandler:).md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](fsreadsymlinkresult.md)
  The result of a read-symlink call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/createlink(to:named:in:context:replyhandler:))*