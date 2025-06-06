# matchesContents(of:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func matchesContents(of url: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when the contents of the file wrapper match the contents of `url`, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The contents of files are not compared; matching of regular files is based on file modification dates. For a directory, children are compared against the files in the directory, recursively.

Because children of directory file wrappers are not read immediately by the [`init(url:options:)`](filewrapper/init(url:options:).md) method unless the `NSFileWrapperReadingImmediate` reading option is used, even a newly-created directory file wrapper might not have the same contents as the directory on disk. You can use this method to determine whether the file wrapper’s contents in memory need to be updated.

If the file wrapper needs updating, use the [`read(from:options:)`](filewrapper/read(from:options:).md) method with the `NSFileWrapperReadingImmediate` reading option.

This table describes which attributes of the file wrapper and file-system node are compared to determine whether the file wrapper matches the node on disk:

| File-wrapper type | Comparison determinants |
| --- | --- |
| Regular file | Modification date and access permissions. |
| Directory | Children (recursive). |
| Symbolic link | Destination pathname. |

## Parameters

- `url`: URL of the file-system node with which to compare the file wrapper.

## See Also

- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [func needsToBeUpdated(fromPath: String) -> Bool](filewrapper/needstobeupdated(frompath:).md)
  Indicates whether the file wrapper needs to be updated to match a given file-system node.
- [func update(fromPath: String) -> Bool](filewrapper/update(frompath:).md)
  Updates the file wrapper to match a given file-system node.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/matchescontents(of:))*