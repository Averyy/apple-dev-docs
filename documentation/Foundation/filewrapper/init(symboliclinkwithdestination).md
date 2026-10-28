# init(symbolicLinkWithDestination:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a symbolic-link file wrapper.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`init(symbolicLinkWithDestinationURL:)`](./init%28symboliclinkwithdestinationurl%29.md) instead.

## Declaration

```swift
convenience init(symbolicLinkWithDestination path: String)
```

```objc
- (id) initSymbolicLinkWithDestination:(NSString *) path;
```

## Return Value

Initialized symbolic-link file wrapper referencing `node`.

## Discussion

The receiver is not associated to a file-system node until you save it using [`write(toFile:atomically:updateFilenames:)`](./write%28tofile,atomically,updatefilenames%29.md). It’s also initialized with open permissions; anyone can read or write the disk representations it saves.

### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`init(symbolicLinkWithDestinationURL:)`](./init%28symboliclinkwithdestinationurl%29.md).

## Parameters

- `path`: Pathname the receiver is to represent.

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
- [init(directoryWithFileWrappers: [String : FileWrapper])](./init%28directorywithfilewrappers%29.md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](./init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](./init%28symboliclinkwithdestinationurl%29.md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](./init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(symboliclinkwithdestination:))*