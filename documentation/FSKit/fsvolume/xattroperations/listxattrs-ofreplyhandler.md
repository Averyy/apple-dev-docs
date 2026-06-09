# listXattrs(of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Gets the list of extended attributes currently set on the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func xattrs(of item: FSItem) async throws -> [FSFileName]
```

## Parameters

- `item`: The item from which to get extended attributes.
- `reply`: A block or closure to indicate success or failure. If getting the list of extended attributes succeeds, pass the xattrs as an array of [`FSFileName`](fsfilename.md) instances and a `nil` error. If getting the attributes fails, pass `nil` along with the relevant error. For an `async` Swift implementation, there’s no reply handler; simply return the byte count or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/listxattrs(of:replyhandler:))*