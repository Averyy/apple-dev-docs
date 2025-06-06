# init(path:)

**Framework**: Foundation  
**Kind**: init

Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init?(path: String)
```

#### Return Value

File wrapper for `node`.

#### Discussion

If `node` is a directory, this method recursively creates file wrappers for each node within that directory.

##### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`init(url:options:)`](filewrapper/init(url:options:).md).

## Parameters

- `path`: Pathname of the file-system node the file wrapper is to represent.

## See Also

- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/init(url:options:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [init(directoryWithFileWrappers: [String : FileWrapper])](filewrapper/init(directorywithfilewrappers:).md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](filewrapper/init(regularfilewithcontents:).md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](filewrapper/init(symboliclinkwithdestination:).md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](filewrapper/init(symboliclinkwithdestinationurl:).md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](filewrapper/init(serializedrepresentation:).md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(path:))*