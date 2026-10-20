# addFile(withPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`addFileWrapper(_:)`](./addfilewrapper%28_%29.md) instead.

## Declaration

```swift
func addFile(withPath path: String) -> String
```

```objc
- (NSString *) addFileWithPath:(NSString *) path;
```

#### Return Value

Dictionary key used to store the new file wrapper in the directory’s list of file wrappers. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information.

#### Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Instead of using this method, you can instantiate `NSFileWrapper` with one of the initializers, set its [`preferredFilename`](./preferredfilename.md) property if necessary, and pass the result to [`addFileWrapper(_:)`](./addfilewrapper%28_%29.md).

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

## Parameters

- `path`: File-System node from which to create the file wrapper to add to the directory.

## See Also

### Accessing File-Wrapper Information
- [var fileWrappers: [String : FileWrapper]?](./filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [func addFileWrapper(FileWrapper) -> String](./addfilewrapper%28_%29.md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [func removeFileWrapper(FileWrapper)](./removefilewrapper%28_%29.md)
  Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [func addRegularFile(withContents: Data, preferredFilename: String) -> String](./addregularfile%28withcontents,preferredfilename%29.md)
  Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [func addSymbolicLink(withDestination: String, preferredFilename: String) -> String](./addsymboliclink%28withdestination,preferredfilename%29.md)
  Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func keyForChildFileWrapper(FileWrapper) -> String?](./keyforchildfilewrapper%28_%29.md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [func symbolicLinkDestination() -> String](./symboliclinkdestination%28%29.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.
- [var symbolicLinkDestinationURL: URL?](./symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/addfile(withpath:))*