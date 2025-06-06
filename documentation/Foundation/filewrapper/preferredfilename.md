# preferredFilename

**Framework**: Foundation  
**Kind**: property

The preferred filename for the file wrapper object.

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
var preferredFilename: String? { get set }
```

#### Discussion

This name is normally used as the dictionary key when a child file wrapper is added to a directory file wrapper. However, if another file wrapper with the same preferred name already exists in the directory file wrapper when this object is added, the filename assigned as the dictionary key may differ from the preferred filename.

When you change the preferred filename, the default implementation of this property causes the existing parent directory file wrappers to remove and re-add the child to accommodate the change. Preferred filenames of children are not preserved when you write a file wrapper to disk and then later instantiate another file wrapper by reading the file from disk. If you need to preserve the user-visible names of attachments, you have to store the names yourself.

## See Also

- [func addFileWrapper(FileWrapper) -> String](filewrapper/addfilewrapper(_:).md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/init(url:options:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [func write(to: URL, options: FileWrapper.WritingOptions, originalContentsURL: URL?) throws](filewrapper/write(to:options:originalcontentsurl:).md)
  Recursively writes the entire contents of a file wrapper to a given file-system URL.
- [init(directoryWithFileWrappers: [String : FileWrapper])](filewrapper/init(directorywithfilewrappers:).md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [var regularFileContents: Data?](filewrapper/regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/preferredfilename)*