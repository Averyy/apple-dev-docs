# fileLength

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The length of the byte source file.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var fileLength: Int64 { get }
```

```objc
@property (nonatomic, readonly) int64_t fileLength;
```

## See Also

### Inspecting a byte source
- [var fileName: String](./filename.md)
  The name of the file for the byte source.
- [var contentType: UTType?](./contenttype.md)
  The format of the byte source file.
- [var relatedFileNamesInSameDirectory: [String]](./relatedfilenamesinsamedirectory.md)
  An array of related file names in the parent directory of the byte source file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/filelength)*