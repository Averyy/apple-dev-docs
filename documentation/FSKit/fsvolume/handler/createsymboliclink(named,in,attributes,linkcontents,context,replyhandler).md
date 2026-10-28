# createSymbolicLink(named:in:attributes:linkContents:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new symbolic link.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func createSymbolicLink(named name: FSFileName, in directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, linkContents contents: FSFileName, context: FSContext, replyHandler reply: @escaping @Sendable (FSCreateSymlinkResult?, (any Error)?) -> Void)
```

```swift
func createSymbolicLink(named name: FSFileName, in directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, linkContents contents: FSFileName, context: FSContext) async throws -> FSCreateSymlinkResult
```

```objc
- (void) createSymbolicLinkNamed:(FSFileName *) name inDirectory:(FSItem *) directory attributes:(FSItemSetAttributesRequest *) newAttributes linkContents:(FSFileName *) contents context:(FSContext *) context replyHandler:(void (^)(FSCreateSymlinkResult *result, NSError *error)) reply;
```

## Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](../../../Foundation/nsposixerrordomain.md) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `contents`: The contents of the new symbolic link.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass an instance of [`FSCreateSymlinkResult`](../../fscreatesymlinkresult.md) containing the newly-created [`FSItem`](../../fsitem.md), its [`FSFileName`](../../fsfilename.md), its [`FSItem.Attributes`](../../fsitem/attributes.md), the updated [`FSItem.Attributes`](../../fsitem/attributes.md) of the parent directory, and the volume’s updated free space, along with a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCreateSymlinkResult`](../../fscreatesymlinkresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

### Working with links
- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](./createlink%28to,named,in,context,replyhandler%29.md)
  Creates a new hard link.
- [class FSCreateLinkResult](../../fscreatelinkresult.md)
  The result of a create-link call.
- [class FSCreateSymlinkResult](../../fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](./readsymboliclink%28_,context,replyhandler%29.md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](../../fsreadsymlinkresult.md)
  The result of a read-symlink call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:))*