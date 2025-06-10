# QLPreviewItem

**Framework**: Quick Look  
**Kind**: protocol

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol QLPreviewItem : NSObjectProtocol
```

## Topics

### Instance Properties
- [var previewItemTitle: String?](qlpreviewitem/previewitemtitle.md)
- [var previewItemURL: URL?](qlpreviewitem/previewitemurl.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [ARQuickLookPreviewItem](arquicklookpreviewitem.md)

## See Also

- [class QLFilePreviewRequest](qlfilepreviewrequest.md)
- [class QLPreviewProvider](qlpreviewprovider.md)
- [class QLPreviewReply](qlpreviewreply.md)
- [class QLPreviewReplyAttachment](qlpreviewreplyattachment.md)
- [protocol QLPreviewingController](qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewitem)*