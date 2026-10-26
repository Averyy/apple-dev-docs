# PDFDocumentDidUnlockNotification

**Framework**: PDFKit  
**Kind**: var  
**Role**: Global Variable

A notification that a document unlocks after a [`unlock(withPassword:)`](./pdfdocument/unlock%28withpassword%29.md) message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```c
extern NSNotificationName const PDFDocumentDidUnlockNotification;
```

#### Discussion

The notification object is the `PDFDocument` object itself.

## See Also

### Notifications
- [PDFDocumentDidBeginFindNotification](./pdfdocumentdidbeginfindnotification.md)
  A notification that the [`beginFindString(_:withOptions:)`](./pdfdocument/beginfindstring%28_,withoptions%29.md) or [`findString(_:withOptions:)`](./pdfdocument/findstring%28_,withoptions%29.md) method begins finding.
- [PDFDocumentDidEndFindNotification](./pdfdocumentdidendfindnotification.md)
  A notification that the [`beginFindString(_:withOptions:)`](./pdfdocument/beginfindstring%28_,withoptions%29.md) or [`findString(_:withOptions:)`](./pdfdocument/findstring%28_,withoptions%29.md) method returns.
- [PDFDocumentDidBeginPageFindNotification](./pdfdocumentdidbeginpagefindnotification.md)
  A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidEndPageFindNotification](./pdfdocumentdidendpagefindnotification.md)
  A notification that a find operation finishes working on a page in a document.
- [PDFDocumentDidFindMatchNotification](./pdfdocumentdidfindmatchnotification.md)
  A notification that a string match is found in a document.
- [PDFDocumentDidBeginWriteNotification](./pdfdocumentdidbeginwritenotification.md)
  A notification that a write operation begins working on a document.
- [PDFDocumentDidEndWriteNotification](./pdfdocumentdidendwritenotification.md)
  A notification that a write operation finishes working on a document.
- [PDFDocumentDidBeginPageWriteNotification](./pdfdocumentdidbeginpagewritenotification.md)
  A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidEndPageWriteNotification](./pdfdocumentdidendpagewritenotification.md)
  A notification that a write operation finishes working on a page in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdidunlocknotification)*