# initForPDFWithPageSize:documentCreationBlock:

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initForPDFWithPageSize:(CGSize) defaultPageSize documentCreationBlock:(PDFDocument * (^)(QLPreviewReply *reply, NSError **error)) documentCreationBlock;
```

## Discussion

Use this method to provide a preview with a PDFDocument

## Parameters

- `defaultPageSize`: The size of your pages in the document. If the page size varies, use the first page’s size.
- `documentCreationBlock`: Create and return the PDFDocument. Heavy lifting should be done inside of the documentCreationBlock instead of when creating the QLPreviewReply. The QLPreviewReply passed into this block is the same as the one created by this method and is provided for convenience for any further updates to its properties during document creation. Return the PDFDocument if successfully created. Populate error if unsuccessful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewreply/initforpdfwithpagesize:documentcreationblock:)*