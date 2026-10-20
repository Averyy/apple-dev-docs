# createLink(to:named:inDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new hard link.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func createLink(to item: FSItem, named name: FSFileName, inDirectory directory: FSItem, replyHandler reply: @escaping @Sendable (FSFileName?, (any Error)?) -> Void)
```

```swift
func createLink(to item: FSItem, named name: FSFileName, inDirectory directory: FSItem) async throws -> FSFileName
```

```objc
- (void) createLinkToItem:(FSItem *) item named:(FSFileName *) name inDirectory:(FSItem *) directory replyHandler:(void (^)(FSFileName *linkName, NSError *error)) reply;
```

#### Discussion

If creating the link fails, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](../../../Foundation/nsposixerrordomain.md) and the following error codes:

- `EEXIST` if there’s already an item named `name` in the directory.
- `EMLINK` if creating the link would exceed the maximum number of hard links supported on `item`.
- `ENOTSUP` if the file system doesn’t support creating hard links to the type of file system object that `item` represents.

## Parameters

- `item`: The existing item to which to link.
- `name`: The name for the new link.
- `directory`: The directory in which to create the link.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass an [`FSFileName`](../../fsfilename.md) of the newly-created link and a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores any [`FSFileName`](../../fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSFileName`](../../fsfilename.md) or throw an error.

## See Also

### Working with links
- [func createSymbolicLink(named: FSFileName, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./createsymboliclink%28named,indirectory,attributes,linkcontents,replyhandler%29.md)
  Creates a new symbolic link.
- [func readSymbolicLink(FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](./readsymboliclink%28_,replyhandler%29.md)
  Reads a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createlink(to:named:indirectory:replyhandler:))*