# PDFDocumentDelegate

**Framework**: PDFKit  
**Kind**: protocol

The delegate for the `PDFDocument` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol PDFDocumentDelegate : NSObjectProtocol
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)

## Topics

### Managing Document Security
- [func documentDidUnlock(Notification)](pdfdocumentdelegate/documentdidunlock(_:).md)
  Called when the `PDFDocumentDidUnlockNotification` notification is posted.
### Getting Document Search Notifications
- [func didMatchString(PDFSelection)](pdfdocumentdelegate/didmatchstring(_:).md)
  Called for every match found during a find operation.
- [func documentDidBeginDocumentFind(Notification)](pdfdocumentdelegate/documentdidbegindocumentfind(_:).md)
  Called when the `PDFDocumentDidBeginFindNotification` notification is posted.
- [func documentDidBeginPageFind(Notification)](pdfdocumentdelegate/documentdidbeginpagefind(_:).md)
  Called when the `PDFDocumentDidBeginPageFindNotification` notification is posted.
- [func documentDidEndDocumentFind(Notification)](pdfdocumentdelegate/documentdidenddocumentfind(_:).md)
  Called when the `PDFDocumentDidEndFindNotification` notification is posted.
- [func documentDidEndPageFind(Notification)](pdfdocumentdelegate/documentdidendpagefind(_:).md)
  Called when the `PDFDocumentDidEndPageFindNotification` notification is posted.
- [func documentDidFindMatch(Notification)](pdfdocumentdelegate/documentdidfindmatch(_:).md)
  Called when the `PDFDocumentDidFindMatchNotification` notification is posted.
### Wrapping Document Elements
- [func classForPage() -> AnyClass](pdfdocumentdelegate/classforpage.md)
  Returns a `PDFPage` subclass for a page object.
- [func `class`(forAnnotationClass: AnyClass) -> AnyClass](pdfdocumentdelegate/class(forannotationclass:).md)
  Returns a `PDFAnnotation` subclass for a class.
- [func `class`(forAnnotationType: String) -> AnyClass](pdfdocumentdelegate/class(forannotationtype:).md)
  Returns a `PDFAnnotation` subclass for an annotation type.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any PDFDocumentDelegate)?](pdfdocument/delegate.md)
  The object acting as the delegate for the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate)*