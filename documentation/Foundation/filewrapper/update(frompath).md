# update(fromPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Updates the file wrapper to match a given file-system node.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`read(from:options:)`](./read%28from,options%29.md) instead.

## Declaration

```swift
func update(fromPath path: String) -> Bool
```

```objc
- (BOOL) updateFromPath:(NSString *) path;
```

## Return Value

[`true`](../../Swift/true.md) if the update is carried out, [`false`](../../Swift/false.md) if it isn’t needed.

## Discussion

For a directory file wrapper, the contained file wrappers are also sent [`update(fromPath:)`](./update%28frompath%29.md) messages. If nodes in the corresponding directory on the file system have been added or removed, corresponding file wrappers are released or created as needed.

### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`read(from:options:)`](./read%28from,options%29.md).

## See Also

### Related Documentation
- [func updateAttachments(fromPath: String)](../nsmutableattributedstring/updateattachments%28frompath%29.md)
  Updates all attachments based on files contained in the RTFD file package at the specified file path.
### Updating File Wrappers
- [func needsToBeUpdated(fromPath: String) -> Bool](./needstobeupdated%28frompath%29.md)
  Indicates whether the file wrapper needs to be updated to match a given file-system node.
- [func matchesContents(of: URL) -> Bool](./matchescontents%28of%29.md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](./read%28from,options%29.md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/update(frompath:))*