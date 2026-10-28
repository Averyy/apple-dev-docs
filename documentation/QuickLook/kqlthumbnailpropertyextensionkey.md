# kQLThumbnailPropertyExtensionKey

**Framework**: Quick Look  
**Kind**: var  
**Role**: Global Variable

The extension to use as a badge when creating an icon.

**Availability**:
- macOS 10.6+ - Deprecated in 12.0

> **Deprecated**: Use a QLThumbnailReply in a Thumbnail Extension to provide thumbnails for your file types.

## Declaration

```swift
let kQLThumbnailPropertyExtensionKey: CFString!
```

```c
extern CFStringRef const kQLThumbnailPropertyExtensionKey;
```

## Discussion

The associated value is a [`CFString`](../CoreFoundation/cfstring.md).

## See Also

### Deprecated constants
- [let kQLPreviewContentIDScheme: CFString!](./kqlpreviewcontentidscheme.md)
  The content ID URL scheme.
- [let kQLPreviewPropertyCursorKey: CFString!](./kqlpreviewpropertycursorkey.md)
- [let kQLPreviewOptionCursorKey: CFString!](./kqlpreviewoptioncursorkey.md)
- [let kQLPreviewPropertyAttachmentDataKey: CFString!](./kqlpreviewpropertyattachmentdatakey.md)
  Attachment data for a preview.
- [let kQLPreviewPropertyAttachmentsKey: CFString!](./kqlpreviewpropertyattachmentskey.md)
  A list of attachments or sub-resources.
- [let kQLPreviewPropertyBaseBundlePathKey: CFString!](./kqlpreviewpropertybasebundlepathkey.md)
  A path that’s outside of the default security scope for creating a preview.
- [let kQLPreviewPropertyDisplayNameKey: CFString!](./kqlpreviewpropertydisplaynamekey.md)
  A custom display name for the preview panel.
- [let kQLPreviewPropertyHeightKey: CFString!](./kqlpreviewpropertyheightkey.md)
  The height in points of the preview.
- [let kQLPreviewPropertyMIMETypeKey: CFString!](./kqlpreviewpropertymimetypekey.md)
  The web content or attachment mime type.
- [let kQLPreviewPropertyPDFStyleKey: CFString!](./kqlpreviewpropertypdfstylekey.md)
  The preferred way to display PDF content.
- [let kQLPreviewPropertyStringEncodingKey: CFString!](./kqlpreviewpropertystringencodingkey.md)
  The string encoding of the preview data.
- [let kQLPreviewPropertyTextEncodingNameKey: CFString!](./kqlpreviewpropertytextencodingnamekey.md)
  The encoding of the web content or attachment text.
- [let kQLPreviewPropertyWidthKey: CFString!](./kqlpreviewpropertywidthkey.md)
  The width in points of the preview.
- [let kQLThumbnailPropertyBadgeImageKey: CFString!](./kqlthumbnailpropertybadgeimagekey.md)
  An image to use for generating the badge for a file’s icon.
- [let kQLThumbnailPropertyBaseBundlePathKey: CFString!](./kqlthumbnailpropertybasebundlepathkey.md)
  A path that’s outside of the default security scope for creating a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/kqlthumbnailpropertyextensionkey)*