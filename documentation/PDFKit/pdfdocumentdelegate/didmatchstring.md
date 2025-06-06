# didMatchString(_:)

**Framework**: PDFKit  
**Kind**: method

Called for every match found during a find operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func didMatchString(_ instance: PDFSelection)
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/didmatchstring(_:))*