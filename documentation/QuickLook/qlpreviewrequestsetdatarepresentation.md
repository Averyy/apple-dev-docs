# QLPreviewRequestSetDataRepresentation(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Sets the preview request to data saved within the document or to dynamically generated data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func QLPreviewRequestSetDataRepresentation(_ preview: QLPreviewRequest!, _ data: CFData!, _ contentTypeUTI: CFString!, _ properties: CFDictionary!)
```

#### Discussion

This function returns preview data to the client. The data is either extracted from a document where the document’s application has saved it, or it’s dynamically generated. How Quick Look handles the data depends upon the value of `contentTypeUTI`. The content data of the preview must be of a native Quick Look type. Currently supported UTIs for these types are: `kUTTypeImage`, `kUTTypePDF`, `kUTTypeHTML`, `kUTTypeXML`, `kUTTypePlainText`, `kUTTypeRTF`, `kUTTypeMovie`, and `kUTTypeAudio`.

If the UTI type is `kUTTypeHTML`, you can have WebKit handle the layout and display of your preview. You must provide the HTML in `data` plus any attachments (for example, Address Book cards, Mail messages, or Omni Outliner documents) in the `properties` dictionary. This dictionary takes [`kQLPreviewPropertyAttachmentsKey`](kqlpreviewpropertyattachmentskey.md) as its key and consists of one ore more subdictionaries (one per attachment). Each subdictionary uses an arbitrary string identifier as a key; the attachment should be referenced within the HTML data using the kQLPreviewContentIDScheme URL scheme (“cid”) and the identifier as the URL resource specifier—for example, “cid:the_identifier”. The keys of the subdictionary properties are [`kQLPreviewPropertyMIMETypeKey`](kqlpreviewpropertymimetypekey.md), [`kQLPreviewPropertyTextEncodingNameKey`](kqlpreviewpropertytextencodingnamekey.md), and [`kQLPreviewPropertyAttachmentDataKey`](kqlpreviewpropertyattachmentdatakey.md).

##### Special Considerations

Thread-safety: This function should be called in the same thread as the preview request is made in; generally, this is the same thread in which the `GeneratePreviewForURL` callback was invoked.

## Parameters

- `preview`: The preview request object.
- `data`: The data of the preview returned to the client.
- `contentTypeUTI`: The UTI specifying the content type of the preview.
- `properties`: Additional properties for the preview response. For more on supported keys and values for this dictionary, see  . If the saved data is HTML, you may specify a special set of properties; see the discussion below for more information.

## See Also

- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](qlpreviewrequestcopycontentuti(_:).md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!](qlpreviewrequestcopyoptions(_:).md)
  Returns the options specified for the preview request.
- [func QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!](qlpreviewrequestcopyurl(_:).md)
  Returns the URL of the document for which a preview is requested.
- [func QLPreviewRequestCreateContext(QLPreviewRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](qlpreviewrequestcreatecontext(_:_:_:_:).md)
  Creates a graphics context to draw the preview in.
- [func QLPreviewRequestCreatePDFContext(QLPreviewRequest!, UnsafePointer<CGRect>!, CFDictionary!, CFDictionary!) -> Unmanaged<CGContext>!](qlpreviewrequestcreatepdfcontext(_:_:_:_:).md)
  Creates a PDF context suitable to draw a multi-page preview.
- [func QLPreviewRequestFlushContext(QLPreviewRequest!, CGContext!)](qlpreviewrequestflushcontext(_:_:).md)
  Flush the context and sets the preview response.
- [func QLPreviewRequestGetDocumentObject(QLPreviewRequest!) -> UnsafeRawPointer!](qlpreviewrequestgetdocumentobject(_:).md)
  Returns the object that’s stored as part of a preview request.
- [func QLPreviewRequestSetDocumentObject(QLPreviewRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](qlpreviewrequestsetdocumentobject(_:_:_:).md)
  Stores an object as part of a preview request.
- [func QLPreviewRequestGetGeneratorBundle(QLPreviewRequest!) -> Unmanaged<CFBundle>!](qlpreviewrequestgetgeneratorbundle(_:).md)
  Get the bundle of the generator receiving the preview request.
- [func QLPreviewRequestGetTypeID() -> CFTypeID](qlpreviewrequestgettypeid().md)
  Gets the type identifier for the `QLPreviewReqest` opaque type.
- [func QLPreviewRequestIsCancelled(QLPreviewRequest!) -> Bool](qlpreviewrequestiscancelled(_:).md)
  Returns whether the preview request has been cancelled by the client.
- [func QLPreviewRequestSetURLRepresentation(QLPreviewRequest!, CFURL!, CFString!, CFDictionary!)](qlpreviewrequestseturlrepresentation(_:_:_:_:).md)
  Sets the contents of the file at the given URL as the response to the preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewrequestsetdatarepresentation(_:_:_:_:))*