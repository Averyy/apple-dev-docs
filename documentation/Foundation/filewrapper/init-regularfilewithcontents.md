# init(regularFileWithContents:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver as a regular-file file wrapper.

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
init(regularFileWithContents contents: Data)
```

#### Return Value

Initialized regular-file file wrapper containing `contents`.

#### Discussion

After initialization, the file wrapper is not associated with a file-system node until you save it using [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md).

The file wrapper is initialized with open permissions: anyone can write to or read the file wrapper.

## Parameters

- `contents`: Contents of the file.

## See Also

- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [var regularFileContents: Data?](filewrapper/regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/init(url:options:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [convenience init?(path: String)](filewrapper/init(path:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(directoryWithFileWrappers: [String : FileWrapper])](filewrapper/init(directorywithfilewrappers:).md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [convenience init(symbolicLinkWithDestination: String)](filewrapper/init(symboliclinkwithdestination:).md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](filewrapper/init(symboliclinkwithdestinationurl:).md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](filewrapper/init(serializedrepresentation:).md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(regularfilewithcontents:))*