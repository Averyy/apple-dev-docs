# needsToBeUpdated(fromPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the file wrapper needs to be updated to match a given file-system node.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`matchesContents(of:)`](./matchescontents%28of%29.md) instead.

## Declaration

```swift
func needsToBeUpdated(fromPath path: String) -> Bool
```

```objc
- (BOOL) needsToBeUpdatedFromPath:(NSString *) path;
```

#### Return Value

[`false`](../../Swift/false.md) when the file wrapper needs to be updated to match `node`, [`false`](../../Swift/false.md) otherwise.

#### Discussion

This table describes which attributes of the file wrapper and `node` are compared to determine whether the file wrapper needs to be updated:

| File-wrapper type | Comparison determinants |
| --- | --- |
| Regular file | Modification date and access permissions. |
| Directory | Member hierarchy (recursive). |
| Symbolic link | Destination pathname. |

##### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`matchesContents(of:)`](./matchescontents%28of%29.md).

## Parameters

- `path`: File-System node with which to compare the file wrapper.

## See Also

### Related Documentation
- [var fileAttributes: [String : Any]](./fileattributes.md)
  A dictionary of file attributes.
### Updating File Wrappers
- [func matchesContents(of: URL) -> Bool](./matchescontents%28of%29.md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func update(fromPath: String) -> Bool](./update%28frompath%29.md)
  Updates the file wrapper to match a given file-system node.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](./read%28from,options%29.md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/needstobeupdated(frompath:))*