# isEntireFileLoaded

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document’s file is completely loaded into memory.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
var isEntireFileLoaded: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the document’s entire file is loaded into memory; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which signifies that the entire file is loaded into memory. You can override this property to return [`false`](https://developer.apple.com/documentation/Swift/false) if additional data needs to be read from the file. `NSDocument` may use this value to do things like prevent volume ejection or warn the user when a partially loaded file disappears from the file system.

## See Also

- [var fileURL: URL?](nsdocument/fileurl.md)
  The location of the document’s on-disk representation.
- [var fileModificationDate: Date?](nsdocument/filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var keepBackupFile: Bool](nsdocument/keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var isDraft: Bool](nsdocument/isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var fileType: String?](nsdocument/filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](nsdocument/isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](nsdocument/isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isentirefileloaded)*