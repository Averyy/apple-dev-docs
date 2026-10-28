# NSFileTypeDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The document type for interpreting the document.

**Availability**:
- macOS 10.6+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSFileTypeDocumentAttribute;
```

## Discussion

The value of this attribute is an [`NSString`](../Foundation/nsstring.md) object indicating which document type was used to interpret the document, specified as a UTI; for reading, this is available along with [`NSDocumentTypeDocumentAttribute`](./nsdocumenttypedocumentattribute.md), but for writing the two are mutually exclusive.

## See Also

### Getting document type keys
- [NSDocumentTypeDocumentAttribute](./nsdocumenttypedocumentattribute.md)
  The document type.
- [NSTextEncodingNameDocumentAttribute](./nstextencodingnamedocumentattribute.md)
  The name of the text encoding to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfiletypedocumentattribute)*