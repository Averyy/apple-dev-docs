# initWithDataOfContentType:contentSize:dataCreationBlock:

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithDataOfContentType:(UTType *) contentType contentSize:(CGSize) contentSize dataCreationBlock:(NSData * (^)(QLPreviewReply *reply, NSError **error)) dataCreationBlock;
```

## Discussion

Use this method to provide a preview with data of a supported format.

## Parameters

- `contentType`: The content type of the data.
- `contentSize`: A hint for the size you would like to display your content at. If your content has an intrinsic size built in, such as images and PDFs, that will be used as the final size, but providing the correct size here will allow QuickLook to present loading UI at the correct size before you are finished creating the data. QuickLook will use a default size if NSZeroSize is passed in.
- `dataCreationBlock`: Create and return data representing the file preview. Supported types include: UTTypeImage, UTTypePDF, UTTypeHTML, UTTypeXML, UTTypePlainText, UTTypeRTF. Heavy lifting should be done inside of the dataCreationBlock instead of when creating the QLPreviewReply. The QLPreviewReply passed into this block is the same as the one created by this method and is provided for convenience for any further updates to its properties, such as attachments, during the data generation. Return the data if successful. Populate error if unsuccessful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewreply/initwithdataofcontenttype:contentsize:datacreationblock:)*