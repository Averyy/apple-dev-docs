# enumerateDirectory(_:startingAt:verifier:attributes:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Enumerates the contents of the given directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func enumerateDirectory(_ directory: FSItem, startingAt cookie: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker) async throws -> FSDirectoryVerifier
```

#### Discussion

This method uses the [`packEntry(name:itemType:itemID:nextCookie:attributes:)`](fsdirectoryentrypacker/packentry(name:itemtype:itemid:nextcookie:attributes:).md) method of the `packer` parameter to deliver the enumerated items to the caller. The general flow of an enumeration implementation follows these steps:

1. Enumeration starts with a call to `enumerateDirectory` using the initial next-cookie and verifier values [`initial`](fsdirectorycookie/initial.md) and [`initial`](fsdirectoryverifier/initial.md), respectively.
2. The implementation uses `packer` to pack the initial set of directory entries. Packing also sets a `nextCookie` to use on the next call.
3. The implementation replies with a new verifier value, a nonzero value that reflects the directory’s current version.
4. On the next call the implementation packs the next set of entries, starting with the item indicated by `cookie`. If `cookie` doesn’t resolve to a valid directory entry, complete the request with an error of domain [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and code [`FSError.Code.invalidDirectoryCookie`](fserror/code/invaliddirectorycookie.md).

When packing, make sure to use acceptable directory entry names and unambiguous input to all file operations that take names without additional normalization, such as`lookupName`.

> 💡 **Tip**: If the `attributes` parameter is `nil`, include at least two entries in a directory: `"."` and `".."`, which represent the current and parent directories, respectively. Both of these items have type [`FSItem.ItemType.directory`](fsitem/itemtype/directory.md). For the root directory, `"."` and `".."` have identical contents. Don’t pack  `"."` and `".."` if `attributes` isn’t `nil`.

## Parameters

- `directory`: The item to enumerate. FSKit guarantees this item is of type  .
- `cookie`: A value that indicates the location within the directory from which to enumerate. Your implementation defines the semantics of the cookie values; they’re opaque to FSKit. The first call to the enumerate method passes   for this parameter. Subsequent calls pass whatever cookie value you previously passed to the packer’s   parmeter.
- `verifier`: A tool to detect whether the directory contents changed since the last call to  . Your implementation defines the semantics of the verifier values; they’re opaque to FSKit. The first call to the enumerate method passes   for this parameter. Subsequent calls pass whatever cookie value you previously passed to the packer’s   parmeter.
- `attributes`: The desired attributes to provide, or   if the caller doesn’t require attributes.
- `packer`: An object that your implementation uses to enumerate directory items, packing one item per callback to  .
- `reply`: A block or closure to indicate success or failure. If enumeration succeeds, pass the current verifier and a   error. If enumeration fails, pass the relevant error as the second parameter; FSKit ignores any verifier in this case. For an   Swift implementation, there’s no reply handler; simply return the current verifier or throw an error.

## See Also

- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [class FSDirectoryEntryPacker](fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/enumeratedirectory(_:startingat:verifier:attributes:packer:replyhandler:))*