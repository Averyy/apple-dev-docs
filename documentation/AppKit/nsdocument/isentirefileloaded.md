# isEntireFileLoaded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document’s file is completely loaded into memory.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
var isEntireFileLoaded: Bool { get }
```

```objc
@property (readonly, getter=isEntireFileLoaded) BOOL entireFileLoaded;
```

#### Return Value

[`true`](../../Swift/true.md) if the document’s entire file is loaded into memory; otherwise [`false`](../../Swift/false.md).

#### Discussion

The default value of this property is [`true`](../../Swift/true.md), which signifies that the entire file is loaded into memory. You can override this property to return [`false`](../../Swift/false.md) if additional data needs to be read from the file. `NSDocument` may use this value to do things like prevent volume ejection or warn the user when a partially loaded file disappears from the file system.

## See Also

### Getting Document Metadata
- [var fileURL: URL?](./fileurl.md)
  The location of the document’s on-disk representation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isentirefileloaded)*