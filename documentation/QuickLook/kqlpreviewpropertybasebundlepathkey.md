# kQLPreviewPropertyBaseBundlePathKey

**Framework**: Quick Look  
**Kind**: var

A path that’s outside of the default security scope for creating a preview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let kQLPreviewPropertyBaseBundlePathKey: CFString!
```

#### Discussion

By default, the Quick Look feature only accepts files within the current document bundle. Use `kQLPreviewPropertyBaseBundlePathKey` to expand the accepted security scope and look at files outside of the current document bundle. The associated value is a path as a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString).

## See Also

- [let kQLPreviewContentIDScheme: CFString!](kqlpreviewcontentidscheme.md)
  The content ID URL scheme.
- [let kQLPreviewPropertyCursorKey: CFString!](kqlpreviewpropertycursorkey.md)
- [let kQLPreviewOptionCursorKey: CFString!](kqlpreviewoptioncursorkey.md)
- [let kQLPreviewPropertyAttachmentDataKey: CFString!](kqlpreviewpropertyattachmentdatakey.md)
  Attachment data for a preview.
- [let kQLPreviewPropertyAttachmentsKey: CFString!](kqlpreviewpropertyattachmentskey.md)
  A list of attachments or sub-resources.
- [let kQLPreviewPropertyDisplayNameKey: CFString!](kqlpreviewpropertydisplaynamekey.md)
  A custom display name for the preview panel.
- [let kQLPreviewPropertyHeightKey: CFString!](kqlpreviewpropertyheightkey.md)
  The height in points of the preview.
- [let kQLPreviewPropertyMIMETypeKey: CFString!](kqlpreviewpropertymimetypekey.md)
  The web content or attachment mime type.
- [let kQLPreviewPropertyPDFStyleKey: CFString!](kqlpreviewpropertypdfstylekey.md)
  The preferred way to display PDF content.
- [let kQLPreviewPropertyStringEncodingKey: CFString!](kqlpreviewpropertystringencodingkey.md)
  The string encoding of the preview data.
- [let kQLPreviewPropertyTextEncodingNameKey: CFString!](kqlpreviewpropertytextencodingnamekey.md)
  The encoding of the web content or attachment text.
- [let kQLPreviewPropertyWidthKey: CFString!](kqlpreviewpropertywidthkey.md)
  The width in points of the preview.
- [let kQLThumbnailPropertyBadgeImageKey: CFString!](kqlthumbnailpropertybadgeimagekey.md)
  An image to use for generating the badge for a file’s icon.
- [let kQLThumbnailPropertyBaseBundlePathKey: CFString!](kqlthumbnailpropertybasebundlepathkey.md)
  A path that’s outside of the default security scope for creating a thumbnail.
- [let kQLThumbnailPropertyExtensionKey: CFString!](kqlthumbnailpropertyextensionkey.md)
  The extension to use as a badge when creating an icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/kqlpreviewpropertybasebundlepathkey)*