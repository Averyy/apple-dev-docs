# QLPreviewReplyAttachment

**Framework**: Quick Look UI  
**Kind**: class

An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class QLPreviewReplyAttachment
```

#### Overview

When providing a data-based Quick Look preview with HTML, use [`QLPreviewReplyAttachment`](qlpreviewreplyattachment.md) to include images, CSS, and other linked content in the HTML of the preview.

Reference content in your html using the `CID` notation for the reference. For instance, if your HTML preview response includes an image, create a [`QLPreviewReplyAttachment`](qlpreviewreplyattachment.md) with the image, add it the reply’s [`attachments`](qlpreviewreply/attachments.md) with an associated string, and reference the image with the associated string, prefixed by `cid:`. The following example illustrates returning HTML as a preview reply with an image as an attachment:

```swift
let reply = QLPreviewReply(dataOfContentType: .html,
                           contentSize: CGSize(width: 750, height: 500)) { htmlReply in
    let content = """
                  <html>
                  <head></head>
                  <body>
                  <h1>Preview</h1>
                  <img src=\"cid:exampleImage\" width=\"400\">
                  </body>
                  </html>
                  """
    guard let contentData = content.data(using: .utf8) else {
        throw PreviewError.previewSetupFailure("Unable to encode preview content")
    }
    guard let imageFileURL = Bundle.main.url(forResource: "yourImage",
                                             withExtension: "jpg") else {
        throw PreviewError.previewSetupFailure("unable to load image")
    }
    let imageData = try Data(contentsOf: imageFileURL)
    
    htmlReply.attachments["exampleImage"] = QLPreviewReplyAttachment(data: imageData,
                                                                     contentType: .jpeg)
    return contentData
}
reply.title = "HTML Preview Example"

```

## Topics

### Creating a preview reply attachment
- [init(data: Data, contentType: UTType)](qlpreviewreplyattachment/init(data:contenttype:).md)
  Creates a preview reply attachment with the specified type.
### Inspecting a preview reply attachment
- [var contentType: UTType](qlpreviewreplyattachment/contenttype.md)
  The content type of the preview attachment.
- [var data: Data](qlpreviewreplyattachment/data.md)
  The data of the preview attachment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class QLPreviewProvider](qlpreviewprovider.md)
  A class that you subclass to provide a data-based Quick Look preview extension.
- [class QLFilePreviewRequest](qlfilepreviewrequest.md)
  A Quick Look preview request that indicates the content to preview.
- [class QLPreviewReply](qlpreviewreply.md)
  The class you create when providing a data-based Quick Look preview extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewreplyattachment)*