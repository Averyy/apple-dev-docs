# QLPreviewReplyAttachment

**Framework**: Quick Look  
**Kind**: class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class QLPreviewReplyAttachment
```

#### Overview

QLPreviewReplyAttachment is used to provide data for attachment in html data-based previews.

## Topics

### Initializers
- [init(data: Data, contentType: UTType)](qlpreviewreplyattachment/init(data:contenttype:).md)
### Instance Properties
- [var contentType: UTType](qlpreviewreplyattachment/contenttype.md)
  The content type of the attachment for an html preview
- [var data: Data](qlpreviewreplyattachment/data.md)
  The data content of an html preview

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class QLFilePreviewRequest](qlfilepreviewrequest.md)
- [class QLPreviewProvider](qlpreviewprovider.md)
- [class QLPreviewReply](qlpreviewreply.md)
- [protocol QLPreviewItem](qlpreviewitem.md)
- [protocol QLPreviewingController](qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewreplyattachment)*