# createLink(to:named:inDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new hard link.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func createLink(to item: FSItem, named name: FSFileName, inDirectory directory: FSItem) async throws -> FSFileName
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
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass an [`FSFileName`](fsfilename.md) of the newly-created link and a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores any [`FSFileName`](fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSFileName`](fsfilename.md) or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createlink(to:named:indirectory:replyhandler:))*