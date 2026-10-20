# PDFViewAnnotationHit

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification posted when the user clicks on an annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let PDFViewAnnotationHit: NSNotification.Name
```

#### Discussion

The notification object is the `PDFView` object itself.

Use the `@”PDFAnnotationHit”` key to obtain userinfo of type `PDFAnnotation *`.

## See Also

### PDFKit
- [static let PDFDocumentDidBeginFind: NSNotification.Name](./pdfdocumentdidbeginfind.md)
  A notification that the document began a find operation.
- [static let PDFDocumentDidBeginPageFind: NSNotification.Name](./pdfdocumentdidbeginpagefind.md)
  A notification that a find operation begins working on a new page of a document.
- [static let PDFDocumentDidBeginPageWrite: NSNotification.Name](./pdfdocumentdidbeginpagewrite.md)
  A notification that a write operation begins working on a page in a document.
- [static let PDFDocumentDidBeginWrite: NSNotification.Name](./pdfdocumentdidbeginwrite.md)
  A notification that a write operation begins working on a document.
- [static let PDFDocumentDidEndFind: NSNotification.Name](./pdfdocumentdidendfind.md)
  A notification that the document finished a find operation.
- [static let PDFDocumentDidEndPageFind: NSNotification.Name](./pdfdocumentdidendpagefind.md)
  A notification that a find operation finishes working on a page in a document.
- [static let PDFDocumentDidEndPageWrite: NSNotification.Name](./pdfdocumentdidendpagewrite.md)
  A notification that a write operation finishes working on a page in a document.
- [static let PDFDocumentDidEndWrite: NSNotification.Name](./pdfdocumentdidendwrite.md)
  A notification that a write operation finishes working on a document.
- [static let PDFDocumentDidFindMatch: NSNotification.Name](./pdfdocumentdidfindmatch.md)
  A notification that a string match is found in a document.
- [static let PDFDocumentDidUnlock: NSNotification.Name](./pdfdocumentdidunlock.md)
  A notification that a document unlocked.
- [static let PDFThumbnailViewDocumentEdited: NSNotification.Name](./pdfthumbnailviewdocumentedited.md)
- [static let PDFViewAnnotationWillHit: NSNotification.Name](./pdfviewannotationwillhit.md)
  A notification posted before the user clicks an annotation.
- [static let PDFViewChangedHistory: NSNotification.Name](./pdfviewchangedhistory.md)
  A notification posted when the page history changes.
- [static let PDFViewCopyPermission: NSNotification.Name](./pdfviewcopypermission.md)
  A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [static let PDFViewDisplayBoxChanged: NSNotification.Name](./pdfviewdisplayboxchanged.md)
  A notification posted when the display box has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/pdfviewannotationhit)*