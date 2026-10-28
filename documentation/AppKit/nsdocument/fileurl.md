# fileURL

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The location of the document’s on-disk representation.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var fileURL: URL? { get set }
```

```objc
@property (copy, nullable) NSURL * fileURL;
```

## Return Value

The document’s location.

## Discussion

The default implementation of this property returns the URL of the file that was opened. Changing the value of this property does not actually change the document’s name or location; it is only for recording the document’s location during its initial opening or saving.

## See Also

### Getting Document Metadata
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
- [var isInViewingMode: Bool](./isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/fileurl)*