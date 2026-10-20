# fileWrappers

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The file wrappers contained by a directory file wrapper.

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
var fileWrappers: [String : FileWrapper]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,NSFileWrapper *> * fileWrappers;
```

#### Discussion

The dictionary contains entries whose values are the file wrappers and whose keys are the unique filenames that have been assigned to each one. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure.

This property may contain `nil` if the user modifies the directory after you call [`read(from:options:)`](./read%28from,options%29.md) or [`init(url:options:)`](./init%28url,options%29-70161.md) but before [`FileWrapper`](../filewrapper.md) has read the contents of the directory.  Use the [`immediate`](./readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

##### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a directory file wrapper.

## See Also

### Related Documentation
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
### Accessing File-Wrapper Information
- [func addFileWrapper(FileWrapper) -> String](./addfilewrapper%28_%29.md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [func removeFileWrapper(FileWrapper)](./removefilewrapper%28_%29.md)
  Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [func addFile(withPath: String) -> String](./addfile%28withpath%29.md)
  Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/filewrappers)*