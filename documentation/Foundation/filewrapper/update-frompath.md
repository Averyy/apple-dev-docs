# update(fromPath:)

**Framework**: Foundation  
**Kind**: method

Updates the file wrapper to match a given file-system node.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func update(fromPath path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the update is carried out, [`false`](https://developer.apple.com/documentation/swift/false) if it isn’t needed.

#### Discussion

For a directory file wrapper, the contained file wrappers are also sent [`update(fromPath:)`](filewrapper/update(frompath:).md) messages. If nodes in the corresponding directory on the file system have been added or removed, corresponding file wrappers are released or created as needed.

##### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`read(from:options:)`](filewrapper/read(from:options:).md).

## See Also

- [func updateAttachments(fromPath: String)](nsmutableattributedstring/updateattachments(frompath:).md)
  Updates all attachments based on files contained in the RTFD file package at the specified file path.
- [func needsToBeUpdated(fromPath: String) -> Bool](filewrapper/needstobeupdated(frompath:).md)
  Indicates whether the file wrapper needs to be updated to match a given file-system node.
- [func matchesContents(of: URL) -> Bool](filewrapper/matchescontents(of:).md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/update(frompath:))*