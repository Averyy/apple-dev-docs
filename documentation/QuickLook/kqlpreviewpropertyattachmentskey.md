# kQLPreviewPropertyAttachmentsKey

**Framework**: Quick Look  
**Kind**: var  
**Role**: Global Variable

A list of attachments or sub-resources.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: Use a QLPreviewingController in a Preview Extension to provide previews for your file types.

## Declaration

```swift
let kQLPreviewPropertyAttachmentsKey: CFString!
```

```c
extern CFStringRef const kQLPreviewPropertyAttachmentsKey;
```

## Discussion

The value is a [`CFDictionary`](../CoreFoundation/cfdictionary.md) object. The keys of the dictionary are the attachment identifiers ([`CFString`](../CoreFoundation/cfstring.md) objects) that can be referenced with the `cid:id` URL. The dictionary’s values are themselves dictionaries that use the [`kQLPreviewPropertyAttachmentDataKey`](./kqlpreviewpropertyattachmentdatakey.md), [`kQLPreviewPropertyMIMETypeKey`](./kqlpreviewpropertymimetypekey.md) and [`kQLPreviewPropertyTextEncodingNameKey`](./kqlpreviewpropertytextencodingnamekey.md) properties.

## See Also

### Deprecated constants
- [let kQLPreviewContentIDScheme: CFString!](./kqlpreviewcontentidscheme.md)
  The content ID URL scheme.
- [let kQLPreviewPropertyCursorKey: CFString!](./kqlpreviewpropertycursorkey.md)
- [let kQLPreviewOptionCursorKey: CFString!](./kqlpreviewoptioncursorkey.md)
- [let kQLPreviewPropertyAttachmentDataKey: CFString!](./kqlpreviewpropertyattachmentdatakey.md)
  Attachment data for a preview.
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
- [let kQLThumbnailPropertyExtensionKey: CFString!](./kqlthumbnailpropertyextensionkey.md)
  The extension to use as a badge when creating an icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/kqlpreviewpropertyattachmentskey)*