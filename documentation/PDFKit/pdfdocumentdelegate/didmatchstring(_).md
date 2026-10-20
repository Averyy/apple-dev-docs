# didMatchString(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) didMatchString:(PDFSelection *) instance;
```

## See Also

### Getting Document Search Notifications
- [func documentDidBeginDocumentFind(Notification)](./documentdidbegindocumentfind%28_%29.md)
  Called when the `PDFDocumentDidBeginFindNotification` notification is posted.
- [func documentDidBeginPageFind(Notification)](./documentdidbeginpagefind%28_%29.md)
  Called when the `PDFDocumentDidBeginPageFindNotification` notification is posted.
- [func documentDidEndDocumentFind(Notification)](./documentdidenddocumentfind%28_%29.md)
  Called when the `PDFDocumentDidEndFindNotification` notification is posted.
- [func documentDidEndPageFind(Notification)](./documentdidendpagefind%28_%29.md)
  Called when the `PDFDocumentDidEndPageFindNotification` notification is posted.
- [func documentDidFindMatch(Notification)](./documentdidfindmatch%28_%29.md)
  Called when the `PDFDocumentDidFindMatchNotification` notification is posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/didmatchstring(_:))*