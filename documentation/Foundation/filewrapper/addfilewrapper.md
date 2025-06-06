# addFileWrapper(_:)

**Framework**: Foundation  
**Kind**: method

Adds a child file wrapper to the receiver, which must be a directory file wrapper.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addFileWrapper(_ child: FileWrapper) -> String
```

#### Return Value

Dictionary key used to store `fileWrapper` in the directory’s list of file wrappers. The dictionary key is a unique filename, which is the same as the passed-in file wrapper’s preferred filename unless that name is already in use as a key in the directory’s dictionary of children. See [`Accessing File Wrapper Identities`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [`File System Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure.

#### Discussion

Use this method to add an existing file wrapper as a child of a directory file wrapper. If the file wrapper does not have a preferred filename, set the [`preferredFilename`](filewrapper/preferredfilename.md) property to give it one before calling [`addFileWrapper(_:)`](filewrapper/addfilewrapper(_:).md). To create a new file wrapper and add it to a directory, use the [`addRegularFile(withContents:preferredFilename:)`](filewrapper/addregularfile(withcontents:preferredfilename:).md) method.

##### Special Considerations

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

This method raises `NSInvalidArgumentException` if the child file wrapper doesn’t have a preferred name.

## Parameters

- `child`: File wrapper to add to the directory.

## See Also

- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var fileWrappers: [String : FileWrapper]?](filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [func removeFileWrapper(FileWrapper)](filewrapper/removefilewrapper(_:).md)
  Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [func addFile(withPath: String) -> String](filewrapper/addfile(withpath:).md)
  Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func addRegularFile(withContents: Data, preferredFilename: String) -> String](filewrapper/addregularfile(withcontents:preferredfilename:).md)
  Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [func addSymbolicLink(withDestination: String, preferredFilename: String) -> String](filewrapper/addsymboliclink(withdestination:preferredfilename:).md)
  Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func keyForChildFileWrapper(FileWrapper) -> String?](filewrapper/keyforchildfilewrapper(_:).md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [func symbolicLinkDestination() -> String](filewrapper/symboliclinkdestination.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.
- [var symbolicLinkDestinationURL: URL?](filewrapper/symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/addfilewrapper(_:))*