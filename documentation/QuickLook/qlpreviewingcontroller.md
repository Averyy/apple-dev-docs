# QLPreviewingController

**Framework**: Quick Look  
**Kind**: protocol  
**Role**: Protocol

For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol QLPreviewingController : NSObjectProtocol
```

```objc
@protocol QLPreviewingController <NSObject>
```

#### Overview

The main preview should be presented by the view controller implementing QLPreviewingController. Avoid presenting additional view controllers over your QLPreviewingController. For Catalyst compatibility, avoid using gesture recognizers that take interactions over large portions of the view to avoid collisions with standard macOS preview behaviors. Avoid holding the file open during the duration of the preview. If access to the file is necessary for interaction, it is best to keep the file open only for the duration of the interaction.

For data-based previews, subclass QLPreviewProvider which conforms to this protocol.

## Topics

### Instance Methods
- [func preparePreviewOfFile(at: URL, completionHandler: ((any Error)?) -> Void)](./qlpreviewingcontroller/preparepreviewoffile%28at,completionhandler%29.md)
- [func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler: ((any Error)?) -> Void)](./qlpreviewingcontroller/preparepreviewofsearchableitem%28identifier,querystring,completionhandler%29.md)
- [func providePreview(for: QLFilePreviewRequest, completionHandler: (QLPreviewReply?, (any Error)?) -> Void)](./qlpreviewingcontroller/providepreview%28for,completionhandler%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### QuickLookUI symbols
- [class QLFilePreviewRequest](./qlfilepreviewrequest.md)
- [class QLPreviewProvider](./qlpreviewprovider.md)
- [class QLPreviewReply](./qlpreviewreply.md)
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
- [protocol QLPreviewItem](./qlpreviewitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewingcontroller)*