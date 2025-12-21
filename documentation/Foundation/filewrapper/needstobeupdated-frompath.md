# needsToBeUpdated(fromPath:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the file wrapper needs to be updated to match a given file-system node.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func needsToBeUpdated(fromPath path: String) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) when the file wrapper needs to be updated to match `node`, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

This table describes which attributes of the file wrapper and `node` are compared to determine whether the file wrapper needs to be updated:

| File-wrapper type | Comparison determinants |
| --- | --- |
| Regular file | Modification date and access permissions. |
| Directory | Member hierarchy (recursive). |
| Symbolic link | Destination pathname. |

##### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`matchesContents(of:)`](filewrapper/matchescontents(of:).md).

## Parameters

- `path`: File-System node with which to compare the file wrapper.

## See Also

- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [func matchesContents(of: URL) -> Bool](filewrapper/matchescontents(of:).md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func update(fromPath: String) -> Bool](filewrapper/update(frompath:).md)
  Updates the file wrapper to match a given file-system node.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/needstobeupdated(frompath:))*