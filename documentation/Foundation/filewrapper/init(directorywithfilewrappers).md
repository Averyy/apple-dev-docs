# init(directoryWithFileWrappers:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a directory file wrapper, with a given file-wrapper list.

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
init(directoryWithFileWrappers childrenByPreferredName: [String : FileWrapper])
```

```objc
- (instancetype) initDirectoryWithFileWrappers:(NSDictionary<NSString *,NSFileWrapper *> *) childrenByPreferredName;
```

## Return Value

Initialized file wrapper for `fileWrappers`.

## Discussion

After initialization, the file wrapper is not associated with a file-system node until you save it using [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md).

The receiver is initialized with open permissions: anyone can read, write, or modify the directory on disk.

If any file wrapper in the directory doesn’t have a preferred filename, its preferred name is automatically set to its corresponding key in the `childrenByPreferredName` dictionary.

## Parameters

- `childrenByPreferredName`: Key-value dictionary of file wrappers with which to initialize the receiver. The dictionary must contain entries whose values are the file wrappers that are to become children and whose keys are filenames. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure.

## See Also

### Related Documentation
- [var preferredFilename: String?](./preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](./fileattributes.md)
  A dictionary of file attributes.
### Creating File Wrappers
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](./init%28url,options%29-70161.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [convenience init?(path: String)](./init%28path%29.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(regularFileWithContents: Data)](./init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](./init%28symboliclinkwithdestination%29.md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](./init%28symboliclinkwithdestinationurl%29.md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](./init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(directorywithfilewrappers:))*