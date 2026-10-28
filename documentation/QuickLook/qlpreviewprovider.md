# QLPreviewProvider

**Framework**: Quick Look  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class QLPreviewProvider
```

```objc
@interface QLPreviewProvider : NSObject
```

## Overview

Data-based preview extensions should subclass QLPreviewProvider in their principal object. The subclass should conform to QLPreviewingController.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### QuickLookUI symbols
- [class QLFilePreviewRequest](./qlfilepreviewrequest.md)
- [class QLPreviewReply](./qlpreviewreply.md)
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
- [protocol QLPreviewItem](./qlpreviewitem.md)
- [protocol QLPreviewingController](./qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewprovider)*