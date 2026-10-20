# QLPreviewProvider

**Framework**: Quick Look UI  
**Kind**: class  
**Role**: Class

A class that you subclass to provide a data-based Quick Look preview extension.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class QLPreviewProvider
```

```objc
@interface QLPreviewProvider : NSObject
```

#### Overview

When you subclass [`QLPreviewProvider`](./qlpreviewprovider.md), conform your subclass to [`QLPreviewingController`](./qlpreviewingcontroller.md).

To provide a data-based Quick Look extension, make the following modifications to your `Info.plist` file:

- Set the Boolean key `QLIsDataBasedPreview` to `true`.
- Add the type identifiers for your extension’s supported content types to the `QLSupportedContentTypes` array.
- Change the value of `NSExtensionPrincipalClass` to the name of your subclass. For example, if you named your subclass `PreviewProvider`, set the value to `$(PRODUCT_MODULE_NAME).PreviewProvider`.

After updating the extension’s `Info.plist` file, implement the [`providePreview(for:completionHandler:)`](./qlpreviewingcontroller/providepreview%28for,completionhandler%29.md) method to return a [`QLPreviewReply`](./qlpreviewreply.md) for the provided [`QLFilePreviewRequest`](./qlfilepreviewrequest.md).

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

### Data-based Preview Extensions
- [class QLFilePreviewRequest](./qlfilepreviewrequest.md)
  A Quick Look preview request that indicates the content to preview.
- [class QLPreviewReply](./qlpreviewreply.md)
  The class you create when providing a data-based Quick Look preview extension.
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
  An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewprovider)*