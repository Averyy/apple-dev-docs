# PDFDocumentDelegate

**Framework**: PDFKit  
**Kind**: protocol  
**Role**: Protocol

The delegate for the `PDFDocument` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
protocol PDFDocumentDelegate : NSObjectProtocol
```

```objc
@protocol PDFDocumentDelegate <NSObject>
```

## Mentions

- [Adding Custom Graphics to a PDF](./adding-custom-graphics-to-a-pdf.md)

## Topics

### Managing Document Security
- [func documentDidUnlock(Notification)](./pdfdocumentdelegate/documentdidunlock%28_%29.md)
  Called when the `PDFDocumentDidUnlockNotification` notification is posted.
### Getting Document Search Notifications
- [func didMatchString(PDFSelection)](./pdfdocumentdelegate/didmatchstring%28_%29.md)
  Called for every match found during a find operation.
- [func documentDidBeginDocumentFind(Notification)](./pdfdocumentdelegate/documentdidbegindocumentfind%28_%29.md)
  Called when the `PDFDocumentDidBeginFindNotification` notification is posted.
- [func documentDidBeginPageFind(Notification)](./pdfdocumentdelegate/documentdidbeginpagefind%28_%29.md)
  Called when the `PDFDocumentDidBeginPageFindNotification` notification is posted.
- [func documentDidEndDocumentFind(Notification)](./pdfdocumentdelegate/documentdidenddocumentfind%28_%29.md)
  Called when the `PDFDocumentDidEndFindNotification` notification is posted.
- [func documentDidEndPageFind(Notification)](./pdfdocumentdelegate/documentdidendpagefind%28_%29.md)
  Called when the `PDFDocumentDidEndPageFindNotification` notification is posted.
- [func documentDidFindMatch(Notification)](./pdfdocumentdelegate/documentdidfindmatch%28_%29.md)
  Called when the `PDFDocumentDidFindMatchNotification` notification is posted.
### Wrapping Document Elements
- [func classForPage() -> AnyClass](./pdfdocumentdelegate/classforpage%28%29.md)
  Returns a `PDFPage` subclass for a page object.
- [func `class`(forAnnotationClass: AnyClass) -> AnyClass](./pdfdocumentdelegate/class%28forannotationclass%29.md)
  Returns a `PDFAnnotation` subclass for a class.
- [func `class`(forAnnotationType: String) -> AnyClass](./pdfdocumentdelegate/class%28forannotationtype%29.md)
  Returns a `PDFAnnotation` subclass for an annotation type.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting the Delegate
- [var delegate: (any PDFDocumentDelegate)?](./pdfdocument/delegate.md)
  The object acting as the delegate for the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate)*