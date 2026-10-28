# NSReadOnlyDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

An indication of whether the document is read-only.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSReadOnlyDocumentAttribute;
```

## Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object that contains an integer. A value of `1` indicates read-only. If the value is `0`, missing, or negative, the document doesn’t display as read-only.

This attribute is not related to the file system protection on the file. Instead, this attribute can affect how the file displays to the user.

The string constant in macOS 10.3 and earlier is `@"ReadOnly"`.

## See Also

### Getting document metadata keys
- [NSAuthorDocumentAttribute](./nsauthordocumentattribute.md)
  The author of the document.
- [NSCategoryDocumentAttribute](./nscategorydocumentattribute.md)
  The document’s category.
- [NSCharacterEncodingDocumentAttribute](./nscharacterencodingdocumentattribute.md)
  The string encoding for the document.
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
- [NSSubjectDocumentAttribute](./nssubjectdocumentattribute.md)
  The subject of the document.
- [NSTitleDocumentAttribute](./nstitledocumentattribute.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsreadonlydocumentattribute)*