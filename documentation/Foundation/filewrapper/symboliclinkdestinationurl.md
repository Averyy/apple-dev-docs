# symbolicLinkDestinationURL

**Framework**: Foundation  
**Kind**: property

The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.

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
var symbolicLinkDestinationURL: URL? { get }
```

#### Discussion

This property may contain `nil` if the user modifies the symbolic link after you call [`read(from:options:)`](filewrapper/read(from:options:).md) or [`init(url:options:)`](filewrapper/init(url:options:).md) but before [`FileWrapper`](filewrapper.md) has read the contents of the link.  Use the [`immediate`](filewrapper/readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

##### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a symbolic-link file wrapper.

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
- [func addSymbolicLink(withDestination: String, preferredFilename: String) -> String](filewrapper/addsymboliclink(withdestination:preferredfilename:).md)
  Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func keyForChildFileWrapper(FileWrapper) -> String?](filewrapper/keyforchildfilewrapper(_:).md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [func symbolicLinkDestination() -> String](filewrapper/symboliclinkdestination.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/symboliclinkdestinationurl)*