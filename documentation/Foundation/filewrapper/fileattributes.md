# fileAttributes

**Framework**: Foundation  
**Kind**: property

A dictionary of file attributes.

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
var fileAttributes: [String : Any] { get set }
```

#### Discussion

The file attributes’ dictionary is the same format as that returned by [`attributesOfItem(atPath:)`](filemanager/attributesofitem(atpath:).md) (`NSFileManager`).

## See Also

- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var regularFileContents: Data?](filewrapper/regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/fileattributes)*