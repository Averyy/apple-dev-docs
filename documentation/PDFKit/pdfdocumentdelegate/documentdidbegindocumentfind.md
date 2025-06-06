# documentDidBeginDocumentFind(_:)

**Framework**: PDFKit  
**Kind**: method

Called when the `PDFDocumentDidBeginFindNotification` notification is posted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func documentDidBeginDocumentFind(_ notification: Notification)
```

## See Also

- [func didMatchString(PDFSelection)](pdfdocumentdelegate/didmatchstring(_:).md)
  Called for every match found during a find operation.
- [func documentDidBeginPageFind(Notification)](pdfdocumentdelegate/documentdidbeginpagefind(_:).md)
  Called when the `PDFDocumentDidBeginPageFindNotification` notification is posted.
- [func documentDidEndDocumentFind(Notification)](pdfdocumentdelegate/documentdidenddocumentfind(_:).md)
  Called when the `PDFDocumentDidEndFindNotification` notification is posted.
- [func documentDidEndPageFind(Notification)](pdfdocumentdelegate/documentdidendpagefind(_:).md)
  Called when the `PDFDocumentDidEndPageFindNotification` notification is posted.
- [func documentDidFindMatch(Notification)](pdfdocumentdelegate/documentdidfindmatch(_:).md)
  Called when the `PDFDocumentDidFindMatchNotification` notification is posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/documentdidbegindocumentfind(_:))*