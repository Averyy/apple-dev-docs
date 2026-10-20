# keepBackupFile

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document archives previously saved versions of the document.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var keepBackupFile: Bool { get }
```

```objc
@property (readonly) BOOL keepBackupFile;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), which causes each new save operation to replace the document’s on-disk content. If you override this method and return [`true`](../../Swift/true.md), a save operation saves the document’s previous contents in a backup file before saving the current contents.

## See Also

### Getting Document Metadata
- [var fileURL: URL?](./fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](./isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](./filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var isDraft: Bool](./isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var fileType: String?](./filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](./isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](./isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/keepbackupfile)*