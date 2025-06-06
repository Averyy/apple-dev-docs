# init(serializedRepresentation:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver as a regular-file file wrapper from given serialized data.

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
init?(serializedRepresentation serializeRepresentation: Data)
```

#### Return Value

Regular-file file wrapper initialized from `serializedRepresentation`.

#### Discussion

The file wrapper is not associated with a file-system node until you save it using [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md).

## Parameters

- `serializeRepresentation`: Serialized representation of a file wrapper in the format used for the   pasteboard type. Data of this format is returned by such methods as   and   ( ).

## See Also

- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/init(url:options:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [convenience init?(path: String)](filewrapper/init(path:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(directoryWithFileWrappers: [String : FileWrapper])](filewrapper/init(directorywithfilewrappers:).md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](filewrapper/init(regularfilewithcontents:).md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](filewrapper/init(symboliclinkwithdestination:).md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](filewrapper/init(symboliclinkwithdestinationurl:).md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(serializedrepresentation:))*