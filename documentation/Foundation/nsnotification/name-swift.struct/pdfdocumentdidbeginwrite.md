# PDFDocumentDidBeginWrite

**Framework**: Foundation  
**Kind**: property

A notification that a write operation begins working on a document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let PDFDocumentDidBeginWrite: NSNotification.Name
```

#### Discussion

The notification object is the `PDFDocument` object itself.

## See Also

- [static let PDFDocumentDidBeginFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginfind.md)
  A notification that the document began a find operation.
- [static let PDFDocumentDidBeginPageFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginpagefind.md)
  A notification that a find operation begins working on a new page of a document.
- [static let PDFDocumentDidBeginPageWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginpagewrite.md)
  A notification that a write operation begins working on a page in a document.
- [static let PDFDocumentDidEndFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendfind.md)
  A notification that the document finished a find operation.
- [static let PDFDocumentDidEndPageFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendpagefind.md)
  A notification that a find operation finishes working on a page in a document.
- [static let PDFDocumentDidEndPageWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendpagewrite.md)
  A notification that a write operation finishes working on a page in a document.
- [static let PDFDocumentDidEndWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendwrite.md)
  A notification that a write operation finishes working on a document.
- [static let PDFDocumentDidFindMatch: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidfindmatch.md)
  A notification that a string match is found in a document.
- [static let PDFDocumentDidUnlock: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidunlock.md)
  A notification that a document unlocked.
- [static let PDFThumbnailViewDocumentEdited: NSNotification.Name](nsnotification/name-swift.struct/pdfthumbnailviewdocumentedited.md)
- [static let PDFViewAnnotationHit: NSNotification.Name](nsnotification/name-swift.struct/pdfviewannotationhit.md)
  A notification posted when the user clicks on an annotation.
- [static let PDFViewAnnotationWillHit: NSNotification.Name](nsnotification/name-swift.struct/pdfviewannotationwillhit.md)
  A notification posted before the user clicks an annotation.
- [static let PDFViewChangedHistory: NSNotification.Name](nsnotification/name-swift.struct/pdfviewchangedhistory.md)
  A notification posted when the page history changes.
- [static let PDFViewCopyPermission: NSNotification.Name](nsnotification/name-swift.struct/pdfviewcopypermission.md)
  A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [static let PDFViewDisplayBoxChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewdisplayboxchanged.md)
  A notification posted when the display box has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidbeginwrite)*