# QLFilePreviewRequest

**Framework**: Quick Look UI  
**Kind**: class  
**Role**: Class

A Quick Look preview request that indicates the content to preview.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class QLFilePreviewRequest
```

```objc
@interface QLFilePreviewRequest : NSObject
```

## Overview

The system provides a [`QLFilePreviewRequest`](./qlfilepreviewrequest.md) to the [`providePreview(for:completionHandler:)`](./qlpreviewingcontroller/providepreview%28for,completionhandler%29.md) method of your data-based Quick Look extension.

## Topics

### Inspecting the preview request
- [var fileURL: URL](./qlfilepreviewrequest/fileurl.md)
  The URL that indicates the content to preview.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data-based Preview Extensions
- [class QLPreviewProvider](./qlpreviewprovider.md)
  A class that you subclass to provide a data-based Quick Look preview extension.
- [class QLPreviewReply](./qlpreviewreply.md)
  The class you create when providing a data-based Quick Look preview extension.
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
  An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlfilepreviewrequest)*