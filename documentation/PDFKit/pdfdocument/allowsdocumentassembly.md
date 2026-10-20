# allowsDocumentAssembly

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether you can manage a document by inserting, deleting, and rotating pages.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var allowsDocumentAssembly: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL allowsDocumentAssembly;
```

## See Also

### Getting Permissions
- [var allowsCopying: Bool](./allowscopying.md)
  A Boolean value indicating whether the document allows copying of content to the Pasteboard.
- [var allowsPrinting: Bool](./allowsprinting.md)
  A Boolean value indicating whether the document allows printing.
- [var allowsCommenting: Bool](./allowscommenting.md)
  A Boolean value indicating whether you can create or modify document annotations, including form field entries.
- [var allowsContentAccessibility: Bool](./allowscontentaccessibility.md)
  A Boolean value indicating whether you can extract content from the document, but only for the purpose of accessibility.
- [var allowsDocumentChanges: Bool](./allowsdocumentchanges.md)
  A Boolean value indicating whether you can modify the document contents except for document attributes.
- [var allowsFormFieldEntry: Bool](./allowsformfieldentry.md)
  A Boolean value indicating whether you can modify form field entries even if you can’t edit document annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/allowsdocumentassembly)*