# filename

**Framework**: Foundation  
**Kind**: property

The filename of the file wrapper object

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
var filename: String? { get set }
```

#### Discussion

This property contains the file wrapper’s filename, or `nil` when the file wrapper has no corresponding file-system node.

The filename is used for record-keeping purposes only and is set automatically when the file wrapper is created from the file system using [`init(url:options:)`](filewrapper/init(url:options:).md) and when it’s saved to the file system using [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md) (although this method allows you to request that the filename not be updated).

The filename is usually the same as the preferred filename, but might instead be a name derived from the preferred filename.  You can use this method to get the name of a child that’s just been read. Don’t use this method to get the name of a child that’s about to be written, because the name might be about to change; send [`keyForChildFileWrapper(_:)`](filewrapper/keyforchildfilewrapper(_:).md) to the parent instead.

## See Also

- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [var regularFileContents: Data?](filewrapper/regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/filename)*