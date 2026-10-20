# lastUsedDate

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The result file’s last-used date.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var lastUsedDate: Date? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * lastUsedDate;
```

## See Also

### Accessing file metadata
- [var creationDate: Date?](./creationdate.md)
  The result file’s creation date.
- [var contentModificationDate: Date?](./contentmodificationdate.md)
  The result file’s content modification date.
- [var contentType: UTType](./contenttype.md)
  The result file’s content type.
- [var documentSize: NSNumber?](./documentsize.md)
  The result file’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult/lastuseddate)*