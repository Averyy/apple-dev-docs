# createSymbolicLink(named:inDirectory:attributes:linkContents:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new symbolic link.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func createSymbolicLink(named name: FSFileName, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, linkContents contents: FSFileName) async throws -> (FSItem, FSFileName)
```

#### Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `contents`: The contents of the new symbolic link.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass the newly-created   and a   error. If creation fails, pass the relevant error as the second parameter; FSKit ignores any   in this case. For an   Swift implementation, there’s no reply handler; simply return the   or throw an error.

## See Also

- [func createLink(to: FSItem, named: FSFileName, inDirectory: FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createlink(to:named:indirectory:replyhandler:).md)
  Creates a new hard link.
- [func readSymbolicLink(FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/readsymboliclink(_:replyhandler:).md)
  Reads a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createsymboliclink(named:indirectory:attributes:linkcontents:replyhandler:))*