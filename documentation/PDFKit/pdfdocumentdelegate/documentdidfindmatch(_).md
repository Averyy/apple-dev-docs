# documentDidFindMatch(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Called when the `PDFDocumentDidFindMatchNotification` notification is posted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func documentDidFindMatch(_ notification: Notification)
```

```objc
- (void) documentDidFindMatch:(NSNotification *) notification;
```

## See Also

### Getting Document Search Notifications
- [func didMatchString(PDFSelection)](./didmatchstring%28_%29.md)
  Called for every match found during a find operation.
- [func documentDidBeginDocumentFind(Notification)](./documentdidbegindocumentfind%28_%29.md)
  Called when the `PDFDocumentDidBeginFindNotification` notification is posted.
- [func documentDidBeginPageFind(Notification)](./documentdidbeginpagefind%28_%29.md)
  Called when the `PDFDocumentDidBeginPageFindNotification` notification is posted.
- [func documentDidEndDocumentFind(Notification)](./documentdidenddocumentfind%28_%29.md)
  Called when the `PDFDocumentDidEndFindNotification` notification is posted.
- [func documentDidEndPageFind(Notification)](./documentdidendpagefind%28_%29.md)
  Called when the `PDFDocumentDidEndPageFindNotification` notification is posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/documentdidfindmatch(_:))*