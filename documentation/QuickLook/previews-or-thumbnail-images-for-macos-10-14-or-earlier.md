# Previews or thumbnail images for macOS 10.14 or earlier

**Framework**: Quick Look  
**Role**: API Collection

Create thumbnail images or previews of common files and custom file types in earlier versions of macOS.

## Overview

The Quick Look framework provides functionality to create a miniature representation, or *thumbnail*, of a file and its contents for display in apps that target macOS 10.14 and earlier.

If your app targets macOS 10.15 and later, use the [Quick Look Thumbnailing](../QuickLookThumbnailing/QuickLookThumbnailing.md) framework to create thumbnails. Similarly, use a Quick Look preview extension to display previews of files instead of Quick Look generators. To learn more, watch [What’s New in File Management and Quick Look](https://developer.apple.com/videos/play/wwdc2019/719).

## Topics

### Creating thumbnails
- [func QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!](./qlthumbnailimagecreate%28_,_,_,_%29.md)
  Creates a thumbnail image for the specified file.
- [func QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!](./qlthumbnailcreate%28_,_,_,_%29.md)
  Returns a thumbnail that’s generated in the background.
- [func QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, (() -> Void)!)](./qlthumbnaildispatchasync%28_,_,_%29.md)
  Creates a thumbnail in the background on the provided background queue.
- [func QLThumbnailCancel(QLThumbnail!)](./qlthumbnailcancel%28_%29.md)
  Cancels the computation of the thumbnail.
- [func QLThumbnailCopyDocumentURL(QLThumbnail!) -> Unmanaged<CFURL>!](./qlthumbnailcopydocumenturl%28_%29.md)
  Returns the URL of the document that you’re requesting a thumbnail for.
- [func QLThumbnailCopyImage(QLThumbnail!) -> Unmanaged<CGImage>!](./qlthumbnailcopyimage%28_%29.md)
  Returns a thumbnail image.
- [func QLThumbnailCopyOptions(QLThumbnail!) -> Unmanaged<CFDictionary>!](./qlthumbnailcopyoptions%28_%29.md)
  Returns the options for the requested thumbnail.
- [func QLThumbnailGetContentRect(QLThumbnail!) -> CGRect](./qlthumbnailgetcontentrect%28_%29.md)
  Returns the rectangle of the provided thumbnail image that represents the content of the document.
- [func QLThumbnailGetMaximumSize(QLThumbnail!) -> CGSize](./qlthumbnailgetmaximumsize%28_%29.md)
  Returns the maximum allowed size for the provided thumbnail image.
- [func QLThumbnailGetTypeID() -> CFTypeID](./qlthumbnailgettypeid%28%29.md)
  Returns the type identifier for the thumbnail’s opaque type.
- [func QLThumbnailIsCancelled(QLThumbnail!) -> Bool](./qlthumbnailiscancelled%28_%29.md)
  Returns whether the creation of the thumbnail was canceled.
### Handling thumbnail requests
- [func QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!](./qlthumbnailrequestcopycontentuti%28_%29.md)
  Returns the UTI for the thumbnail request.
- [func QLThumbnailRequestCopyOptions(QLThumbnailRequest!) -> Unmanaged<CFDictionary>!](./qlthumbnailrequestcopyoptions%28_%29.md)
  Returns the options specified for the thumbnail request.
- [func QLThumbnailRequestCopyURL(QLThumbnailRequest!) -> Unmanaged<CFURL>!](./qlthumbnailrequestcopyurl%28_%29.md)
  Returns the URL of the document for which the thumbnail request is requested.
- [func QLThumbnailRequestCreateContext(QLThumbnailRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](./qlthumbnailrequestcreatecontext%28_,_,_,_%29.md)
  Creates a graphics context to draw the thumbnail in.
- [func QLThumbnailRequestFlushContext(QLThumbnailRequest!, CGContext!)](./qlthumbnailrequestflushcontext%28_,_%29.md)
  Flush the graphics context and sets the thumbnail response.
- [func QLThumbnailRequestGetDocumentObject(QLThumbnailRequest!) -> UnsafeRawPointer!](./qlthumbnailrequestgetdocumentobject%28_%29.md)
  Returns the object that’s stored as part of a thumbnail request.
- [func QLThumbnailRequestGetGeneratorBundle(QLThumbnailRequest!) -> Unmanaged<CFBundle>!](./qlthumbnailrequestgetgeneratorbundle%28_%29.md)
  Get the bundle of the generator receiving the thumbnail request.
- [func QLThumbnailRequestGetMaximumSize(QLThumbnailRequest!) -> CGSize](./qlthumbnailrequestgetmaximumsize%28_%29.md)
  Returns the maximum size (in points) specified for the thumbnail image.
- [func QLThumbnailRequestGetTypeID() -> CFTypeID](./qlthumbnailrequestgettypeid%28%29.md)
  Gets the type identifier for the `QLThumbnailRequest` opaque type.
- [func QLThumbnailRequestIsCancelled(QLThumbnailRequest!) -> Bool](./qlthumbnailrequestiscancelled%28_%29.md)
  Returns whether the thumbnail request has been cancelled by the client.
- [func QLThumbnailRequestSetDocumentObject(QLThumbnailRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](./qlthumbnailrequestsetdocumentobject%28_,_,_%29.md)
  Stores an object as part of a thumbnail request.
- [func QLThumbnailRequestSetImage(QLThumbnailRequest!, CGImage!, CFDictionary!)](./qlthumbnailrequestsetimage%28_,_,_%29.md)
  Sets the thumbnail request to a specified image.
- [func QLThumbnailRequestSetImageAtURL(QLThumbnailRequest!, CFURL!, CFDictionary!)](./qlthumbnailrequestsetimageaturl%28_,_,_%29.md)
  Sets the thumbnail request to contain the image at a given URL.
- [func QLThumbnailRequestSetImageWithData(QLThumbnailRequest!, CFData!, CFDictionary!)](./qlthumbnailrequestsetimagewithdata%28_,_,_%29.md)
  Sets the response to the thumbnail request to image data saved within the document.
- [func QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)](./qlthumbnailrequestsetthumbnailwithdatarepresentation%28_,_,_,_,_%29.md)
  Sets the default image representation for an item with the provided data and specified file type.
- [func QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)](./qlthumbnailrequestsetthumbnailwithurlrepresentation%28_,_,_,_,_%29.md)
  Sets the default image representation for an item of a given type at the specified URL.
### Requesting previews
- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](./qlpreviewrequestcopycontentuti%28_%29.md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!](./qlpreviewrequestcopyoptions%28_%29.md)
  Returns the options specified for the preview request.
- [func QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!](./qlpreviewrequestcopyurl%28_%29.md)
  Returns the URL of the document for which a preview is requested.
- [func QLPreviewRequestCreateContext(QLPreviewRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](./qlpreviewrequestcreatecontext%28_,_,_,_%29.md)
  Creates a graphics context to draw the preview in.
- [func QLPreviewRequestCreatePDFContext(QLPreviewRequest!, UnsafePointer<CGRect>!, CFDictionary!, CFDictionary!) -> Unmanaged<CGContext>!](./qlpreviewrequestcreatepdfcontext%28_,_,_,_%29.md)
  Creates a PDF context suitable to draw a multi-page preview.
- [func QLPreviewRequestFlushContext(QLPreviewRequest!, CGContext!)](./qlpreviewrequestflushcontext%28_,_%29.md)
  Flush the context and sets the preview response.
- [func QLPreviewRequestGetDocumentObject(QLPreviewRequest!) -> UnsafeRawPointer!](./qlpreviewrequestgetdocumentobject%28_%29.md)
  Returns the object that’s stored as part of a preview request.
- [func QLPreviewRequestSetDocumentObject(QLPreviewRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](./qlpreviewrequestsetdocumentobject%28_,_,_%29.md)
  Stores an object as part of a preview request.
- [func QLPreviewRequestGetGeneratorBundle(QLPreviewRequest!) -> Unmanaged<CFBundle>!](./qlpreviewrequestgetgeneratorbundle%28_%29.md)
  Get the bundle of the generator receiving the preview request.
- [func QLPreviewRequestGetTypeID() -> CFTypeID](./qlpreviewrequestgettypeid%28%29.md)
  Gets the type identifier for the `QLPreviewReqest` opaque type.
- [func QLPreviewRequestIsCancelled(QLPreviewRequest!) -> Bool](./qlpreviewrequestiscancelled%28_%29.md)
  Returns whether the preview request has been cancelled by the client.
- [func QLPreviewRequestSetDataRepresentation(QLPreviewRequest!, CFData!, CFString!, CFDictionary!)](./qlpreviewrequestsetdatarepresentation%28_,_,_,_%29.md)
  Sets the preview request to data saved within the document or to dynamically generated data.
- [func QLPreviewRequestSetURLRepresentation(QLPreviewRequest!, CFURL!, CFString!, CFDictionary!)](./qlpreviewrequestseturlrepresentation%28_,_,_,_%29.md)
  Sets the contents of the file at the given URL as the response to the preview request.
### Configuring the appearance of PDF previews
- [struct QLPreviewPDFStyle](./qlpreviewpdfstyle.md)
  A value you use to configure the appearance of previews for PDF files.
### Interfacing with a Quick Look plug-in
- [struct QLGeneratorInterfaceStruct](./qlgeneratorinterfacestruct.md)
  An opaque reference that provides callbacks that the platform uses to interface with a Quick Look plug-in.
### Opaque types
- [class QLThumbnail](./qlthumbnail.md)
  An opaque reference that represents a thumbnail object.
- [class QLThumbnailRequest](./qlthumbnailrequest.md)
  An opaque reference that represents a thumbnail request object.
- [class QLPreviewRequest](./qlpreviewrequest.md)
  An opaque reference that represents a preview request object.
### Constants
- [var kQLReturnMask: Int32](./kqlreturnmask.md)
  The Quick Look generator can create a preview.
- [var kQLReturnHasMore: Int32](./kqlreturnhasmore.md)
  The Quick Look generator has more content to display as part of the preview.
- [let kQLThumbnailOptionIconModeKey: CFString!](./kqlthumbnailoptioniconmodekey.md)
  The Quick Look generator produces the thumbnail as an icon with decor.
- [let kQLThumbnailOptionScaleFactorKey: CFString!](./kqlthumbnailoptionscalefactorkey.md)
  The scale factor for the thumbnail.
- [var QUICKLOOK_VERSION: Int32](./quicklook_version.md)
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
- [let kQLThumbnailPropertyExtensionKey: CFString!](./kqlthumbnailpropertyextensionkey.md)
  The extension to use as a badge when creating an icon.
### QuickLookUI symbols
- [class QLFilePreviewRequest](./qlfilepreviewrequest.md)
- [class QLPreviewProvider](./qlpreviewprovider.md)
- [class QLPreviewReply](./qlpreviewreply.md)
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
- [protocol QLPreviewItem](./qlpreviewitem.md)
- [protocol QLPreviewingController](./qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.
### Macros
- [QL_DEPRECATED](./ql_deprecated.md)
- [QL_EXPORT](./ql_export.md)
- [QL_EXPORT_OSX](./ql_export_osx.md)
- [QL_EXTERN_C_BEGIN](./ql_extern_c_begin.md)
- [QL_EXTERN_C_END](./ql_extern_c_end.md)
- [QL_FORMAT_ARG](./ql_format_arg.md)
- [QL_INLINE](./ql_inline.md)
- [QL_NOINLINE](./ql_noinline.md)
- [QL_PRIVATE_EXPORT](./ql_private_export.md)
- [kQLGeneratorCallbacksInterfaceID](./kqlgeneratorcallbacksinterfaceid.md)
- [kQLGeneratorTypeID](./kqlgeneratortypeid.md)
- [kQLReturnNoError](./kqlreturnnoerror.md)

## See Also

### Previews
- [class QLPreviewController](./qlpreviewcontroller.md)
  A specialized view controller for previewing an item.
- [protocol QLPreviewItem](../QuickLookUI/qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your app’s content.
- [class QLPreviewSceneActivationConfiguration](./qlpreviewsceneactivationconfiguration.md)
  A scene configuration to preview items at the specified URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previews-or-thumbnail-images-for-macos-10-14-or-earlier)*