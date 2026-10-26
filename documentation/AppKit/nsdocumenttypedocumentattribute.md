# NSDocumentTypeDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The document type.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSDocumentTypeDocumentAttribute;
```

#### Discussion

The value of this attribute is one of the document types declared in [`NSAttributedStringDocumentType`](./nsattributedstringdocumenttype.md). For reader methods, this key in options can specify the document type for interpreting the contents. Upon return, the document attributes can contain this key for indicating the actual format used to read the contents. For write methods, this key specifies the format for generating the data.

The string constant in macOS 10.3 and earlier is `@"DocumentType"`.

## See Also

### Getting document type keys
- [NSFileTypeDocumentAttribute](./nsfiletypedocumentattribute.md)
  The document type for interpreting the document.
- [NSTextEncodingNameDocumentAttribute](./nstextencodingnamedocumentattribute.md)
  The name of the text encoding to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumenttypedocumentattribute)*