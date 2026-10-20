# isDocumentEdited

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document has unsaved changes.

**Availability**:
- macOS

## Declaration

```swift
var isDocumentEdited: Bool { get }
```

```objc
@property (readonly, getter=isDocumentEdited) BOOL documentEdited;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the document has been edited. The edited status of each document window reflects the document’s edited status.

## See Also

### Related Documentation
- [func updateChangeCount(NSDocument.ChangeType)](./updatechangecount%28_%29.md)
  Updates the receiver’s change count according to the given change type.
- [var isDocumentEdited: Bool](../nswindow/isdocumentedited.md)
  A Boolean value that indicates whether the window’s document has been edited.
### Getting Document Metadata
- [var fileURL: URL?](./fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](./isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](./filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var keepBackupFile: Bool](./keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var isDraft: Bool](./isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var fileType: String?](./filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isInViewingMode: Bool](./isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isdocumentedited)*