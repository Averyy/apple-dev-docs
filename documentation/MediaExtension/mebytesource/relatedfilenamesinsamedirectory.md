# relatedFileNamesInSameDirectory

**Framework**: MediaExtension  
**Kind**: property

An array of related file names in the parent directory of the byte source file.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var relatedFileNamesInSameDirectory: [String] { get }
```

#### Discussion

The array of related files within the [`MEByteSource`](mebytesource.md)’s parent directory that are accessible to the [`MEByteSource`](mebytesource.md). Only the relative file names are returned, not the paths. Only files with file extensions listed in the [`kMEFormatReaderFileNameExtensionArrayKey`](kmeformatreaderfilenameextensionarraykey.md) array in the format reader property list will be returned. If no related files are available, returns an empty array.

## See Also

- [var fileName: String](mebytesource/filename.md)
  The name of the file for the byte source.
- [var fileLength: Int64](mebytesource/filelength.md)
  The length of the byte source file.
- [var contentType: UTType?](mebytesource/contenttype.md)
  The format of the byte source file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/relatedfilenamesinsamedirectory)*