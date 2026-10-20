# contentType

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The result file’s content type.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@NSCopying
var contentType: UTType { get }
```

```objc
@property (nonatomic, copy, readonly) UTType * contentType;
```

## See Also

### Accessing file metadata
- [var creationDate: Date?](./creationdate.md)
  The result file’s creation date.
- [var contentModificationDate: Date?](./contentmodificationdate.md)
  The result file’s content modification date.
- [var lastUsedDate: Date?](./lastuseddate.md)
  The result file’s last-used date.
- [var documentSize: NSNumber?](./documentsize.md)
  The result file’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult/contenttype)*