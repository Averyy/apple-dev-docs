# NSCharacterEncodingDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The string encoding for the document.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSCharacterEncodingDocumentAttribute;
```

#### Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing integer specifying [`NSStringEncoding`](../Foundation/nsstringencoding.md) for the file; default for plain text is the default encoding. This key in options can specify the string encoding for reading the data. Upon return, the document attributes can contain the actual encoding used. For writing methods, this value is used for generating the plain text data.

The string constant in macOS 10.3 and earlier is `@"CharacterEncoding"`.

## See Also

### Getting document metadata keys
- [NSAuthorDocumentAttribute](./nsauthordocumentattribute.md)
  The author of the document.
- [NSCategoryDocumentAttribute](./nscategorydocumentattribute.md)
  The document’s category.
- [NSCocoaVersionDocumentAttribute](./nscocoaversiondocumentattribute.md)
  The version of Cocoa that created the file.
- [NSCommentDocumentAttribute](./nscommentdocumentattribute.md)
  The document comments.
- [NSCompanyDocumentAttribute](./nscompanydocumentattribute.md)
  The company or organization name associated with the document.
- [NSConvertedDocumentAttribute](./nsconverteddocumentattribute.md)
  A value that indicates whether a filter service converted the file.
- [NSCopyrightDocumentAttribute](./nscopyrightdocumentattribute.md)
  The document’s copyright information.
- [NSCreationTimeDocumentAttribute](./nscreationtimedocumentattribute.md)
  The creation date of the document.
- [NSEditorDocumentAttribute](./nseditordocumentattribute.md)
  The name of person who last edited the document.
- [NSKeywordsDocumentAttribute](./nskeywordsdocumentattribute.md)
  The document keywords.
- [NSManagerDocumentAttribute](./nsmanagerdocumentattribute.md)
  The name of the author’s manager.
- [NSModificationTimeDocumentAttribute](./nsmodificationtimedocumentattribute.md)
  The modification date of the document.
- [NSReadOnlyDocumentAttribute](./nsreadonlydocumentattribute.md)
  An indication of whether the document is read-only.
- [NSSubjectDocumentAttribute](./nssubjectdocumentattribute.md)
  The subject of the document.
- [NSTitleDocumentAttribute](./nstitledocumentattribute.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscharacterencodingdocumentattribute)*