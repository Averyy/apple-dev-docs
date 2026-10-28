# symbolicLinkDestination()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`symbolicLinkDestinationURL`](./symboliclinkdestinationurl.md) instead.

## Declaration

```swift
func symbolicLinkDestination() -> String
```

```objc
- (NSString *) symbolicLinkDestination;
```

## Return Value

Pathname the file wrapper references (the destination of the symbolic link the file wrapper represents).

## Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`symbolicLinkDestinationURL`](./symboliclinkdestinationurl.md).

This method raises `NSInternalInconsistencyException` if the receiver is not a symbolic-link file wrapper.

## See Also

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
- [func keyForChildFileWrapper(FileWrapper) -> String?](./keyforchildfilewrapper%28_%29.md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [var symbolicLinkDestinationURL: URL?](./symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/symboliclinkdestination())*