# documentSize

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The result file’s size.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@NSCopying
var documentSize: NSNumber? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * documentSize;
```

## See Also

### Accessing file metadata
- [var creationDate: Date?](./creationdate.md)
  The result file’s creation date.
- [var contentModificationDate: Date?](./contentmodificationdate.md)
  The result file’s content modification date.
- [var lastUsedDate: Date?](./lastuseddate.md)
  The result file’s last-used date.
- [var contentType: UTType](./contenttype.md)
  The result file’s content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult/documentsize)*