# fileName

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The name of the file for the byte source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var fileName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * fileName;
```

## See Also

### Inspecting a byte source
- [var fileLength: Int64](./filelength.md)
  The length of the byte source file.
- [var contentType: UTType?](./contenttype.md)
  The format of the byte source file.
- [var relatedFileNamesInSameDirectory: [String]](./relatedfilenamesinsamedirectory.md)
  An array of related file names in the parent directory of the byte source file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/filename)*