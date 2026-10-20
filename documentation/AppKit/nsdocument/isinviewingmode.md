# isInViewingMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document is in read-only mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isInViewingMode: Bool { get }
```

```objc
@property (readonly, getter=isInViewingMode) BOOL inViewingMode;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the document is in read-only “viewing mode,” that is, if the document is locked. You can use this information to prevent certain kinds of user actions or changes when the user is viewing an old document revision.

## See Also

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
- [var isDocumentEdited: Bool](./isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isinviewingmode)*