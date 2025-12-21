# kQLPreviewPropertyStringEncodingKey

**Framework**: Quick Look  
**Kind**: var

The string encoding of the preview data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
let kQLPreviewPropertyStringEncodingKey: CFString!
```

#### Discussion

Specifies the string encoding of the preview data as an [`CFStringEncoding`](https://developer.apple.com/documentation/CoreFoundation/CFStringEncoding) if the native type is plain text. You must encapsulate the value in a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object.

## See Also

- [let kQLPreviewContentIDScheme: CFString!](kqlpreviewcontentidscheme.md)
  The content ID URL scheme.
- [let kQLPreviewPropertyCursorKey: CFString!](kqlpreviewpropertycursorkey.md)
- [let kQLPreviewOptionCursorKey: CFString!](kqlpreviewoptioncursorkey.md)
- [let kQLPreviewPropertyAttachmentDataKey: CFString!](kqlpreviewpropertyattachmentdatakey.md)
  Attachment data for a preview.
- [let kQLPreviewPropertyAttachmentsKey: CFString!](kqlpreviewpropertyattachmentskey.md)
  A list of attachments or sub-resources.
- [let kQLPreviewPropertyBaseBundlePathKey: CFString!](kqlpreviewpropertybasebundlepathkey.md)
  A path that’s outside of the default security scope for creating a preview.
- [let kQLPreviewPropertyDisplayNameKey: CFString!](kqlpreviewpropertydisplaynamekey.md)
  A custom display name for the preview panel.
- [let kQLPreviewPropertyHeightKey: CFString!](kqlpreviewpropertyheightkey.md)
  The height in points of the preview.
- [let kQLPreviewPropertyMIMETypeKey: CFString!](kqlpreviewpropertymimetypekey.md)
  The web content or attachment mime type.
- [let kQLPreviewPropertyPDFStyleKey: CFString!](kqlpreviewpropertypdfstylekey.md)
  The preferred way to display PDF content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/kqlpreviewpropertystringencodingkey)*