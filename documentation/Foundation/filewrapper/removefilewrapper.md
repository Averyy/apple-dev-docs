# removeFileWrapper(_:)

**Framework**: Foundation  
**Kind**: method

Removes a child file wrapper from the receiver, which must be a directory file wrapper.

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
func removeFileWrapper(_ child: FileWrapper)
```

#### Discussion

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

## Parameters

- `child`: File wrapper to remove from the directory.

## See Also

- [var fileWrappers: [String : FileWrapper]?](filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [func addFileWrapper(FileWrapper) -> String](filewrapper/addfilewrapper(_:).md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/removefilewrapper(_:))*