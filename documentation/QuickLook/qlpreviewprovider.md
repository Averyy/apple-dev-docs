# QLPreviewProvider

**Framework**: Quick Look  
**Kind**: class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class QLPreviewProvider
```

#### Overview

Data-based preview extensions should subclass QLPreviewProvider in their principal object. The subclass should conform to QLPreviewingController.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class QLFilePreviewRequest](qlfilepreviewrequest.md)
- [class QLPreviewReply](qlpreviewreply.md)
- [class QLPreviewReplyAttachment](qlpreviewreplyattachment.md)
- [protocol QLPreviewItem](qlpreviewitem.md)
- [protocol QLPreviewingController](qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewprovider)*