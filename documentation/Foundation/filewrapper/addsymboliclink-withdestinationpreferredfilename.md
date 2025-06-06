# addSymbolicLink(withDestination:preferredFilename:)

**Framework**: Foundation  
**Kind**: method

Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func addSymbolicLink(withDestination path: String, preferredFilename filename: String) -> String
```

#### Return Value

Dictionary key used to store the new file wrapper in the directory’s list of file wrappers. See [`Accessing File Wrapper Identities`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [`File System Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information.

#### Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Instead of using this method, you can instantiate `NSFileWrapper` with one of the initializers, set its [`preferredFilename`](filewrapper/preferredfilename.md) property if necessary, and pass the result to [`addFileWrapper(_:)`](filewrapper/addfilewrapper(_:).md).

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

This method raises `NSInvalidArgumentException` if you pass `nil` or an empty value for `preferredFilename`.

## Parameters

- `path`: Pathname the new symbolic-link file wrapper is to reference.
- `filename`: Preferred filename for the new symbolic-link file wrapper.

## See Also

- [var fileWrappers: [String : FileWrapper]?](filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [func addFileWrapper(FileWrapper) -> String](filewrapper/addfilewrapper(_:).md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [func removeFileWrapper(FileWrapper)](filewrapper/removefilewrapper(_:).md)
  Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [func addFile(withPath: String) -> String](filewrapper/addfile(withpath:).md)
  Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func addRegularFile(withContents: Data, preferredFilename: String) -> String](filewrapper/addregularfile(withcontents:preferredfilename:).md)
  Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [func keyForChildFileWrapper(FileWrapper) -> String?](filewrapper/keyforchildfilewrapper(_:).md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [func symbolicLinkDestination() -> String](filewrapper/symboliclinkdestination.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.
- [var symbolicLinkDestinationURL: URL?](filewrapper/symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/addsymboliclink(withdestination:preferredfilename:))*