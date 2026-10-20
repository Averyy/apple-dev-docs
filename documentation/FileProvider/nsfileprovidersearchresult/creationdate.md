# creationDate

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The result file’s creation date.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var creationDate: Date? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * creationDate;
```

## See Also

### Accessing file metadata
- [var contentModificationDate: Date?](./contentmodificationdate.md)
  The result file’s content modification date.
- [var lastUsedDate: Date?](./lastuseddate.md)
  The result file’s last-used date.
- [var contentType: UTType](./contenttype.md)
  The result file’s content type.
- [var documentSize: NSNumber?](./documentsize.md)
  The result file’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult/creationdate)*