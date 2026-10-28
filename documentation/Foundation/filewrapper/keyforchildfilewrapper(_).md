# keyForChildFileWrapper(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the dictionary key used by a directory to identify a given file wrapper.

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
func keyForChildFileWrapper(_ child: FileWrapper) -> String?
```

```objc
- (NSString *) keyForFileWrapper:(NSFileWrapper *) child;
```

## Return Value

Dictionary key used to store the file wrapper in the directory’s list of file wrappers. The dictionary key is a unique filename, which may not be the same as the passed-in file wrapper’s preferred filename if more than one file wrapper in the directory’s dictionary of children has the same preferred filename. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure. Returns `nil` if the file wrapper specified in `child` is not a child of the directory.

## Discussion

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

## Parameters

- `child`: The child file wrapper for which you want the key.

## See Also

### Related Documentation
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
### Accessing File-Wrapper Information
- [var fileWrappers: [String : FileWrapper]?](./filewrappers.md)
  The file wrappers contained by a directory file wrapper.
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
- [func symbolicLinkDestination() -> String](./symboliclinkdestination%28%29.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.
- [var symbolicLinkDestinationURL: URL?](./symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/keyforchildfilewrapper(_:))*