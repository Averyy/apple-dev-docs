# regularFileContents

**Framework**: Foundation  
**Kind**: property

The contents of the file-system node associated with a regular-file file wrapper.

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
var regularFileContents: Data? { get }
```

#### Discussion

This property may contain `nil` if the user modifies the file after you call [`read(from:options:)`](filewrapper/read(from:options:).md) or [`init(url:options:)`](filewrapper/init(url:options:).md) but before [`FileWrapper`](filewrapper.md) has read the contents of the file. Use the [`immediate`](filewrapper/readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

##### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a regular-file file wrapper.

## See Also

- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [init(regularFileWithContents: Data)](filewrapper/init(regularfilewithcontents:).md)
  Initializes the receiver as a regular-file file wrapper.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/regularfilecontents)*