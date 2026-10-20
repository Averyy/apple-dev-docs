# init(path:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`init(url:options:)`](./init%28url,options%29-70161.md) instead.

## Declaration

```swift
convenience init?(path: String)
```

```objc
- (id) initWithPath:(NSString *) path;
```

#### Return Value

File wrapper for `node`.

#### Discussion

If `node` is a directory, this method recursively creates file wrappers for each node within that directory.

##### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`init(url:options:)`](./init%28url,options%29-70161.md).

## Parameters

- `path`: Pathname of the file-system node the file wrapper is to represent.

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
- [init(directoryWithFileWrappers: [String : FileWrapper])](./init%28directorywithfilewrappers%29.md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](./init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](./init%28symboliclinkwithdestination%29.md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](./init%28symboliclinkwithdestinationurl%29.md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](./init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(path:))*