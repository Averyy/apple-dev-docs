# NSCharacterEncodingDocumentAttribute

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The string encoding for the document.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey const NSCharacterEncodingDocumentAttribute;
```

## Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing an integer specifying [`NSStringEncoding`](../Foundation/nsstringencoding.md) for the file; default for plain text is the default encoding. This key in options can specify the string encoding for reading the data. Upon return, the document attributes can contain the actual encoding used. For writing methods, this value is used for generating the plain text data.

The string constant in macOS 10.3 and earlier is `@"CharacterEncoding"`.

## See Also

### Getting document metadata keys
- [NSAuthorDocumentAttribute](../AppKit/nsauthordocumentattribute.md)
  The author of the document.
- [NSCategoryDocumentAttribute](../AppKit/nscategorydocumentattribute.md)
  The document’s category.
- [NSCocoaVersionDocumentAttribute](./nscocoaversiondocumentattribute.md)
  The version of Cocoa that created the file.
- [NSCommentDocumentAttribute](../AppKit/nscommentdocumentattribute.md)
  The document comments.
- [NSCompanyDocumentAttribute](../AppKit/nscompanydocumentattribute.md)
  The company or organization name associated with the document.
- [NSConvertedDocumentAttribute](../AppKit/nsconverteddocumentattribute.md)
  A value that indicates whether a filter service converted the file.
- [NSCopyrightDocumentAttribute](../AppKit/nscopyrightdocumentattribute.md)
  The document’s copyright information.
- [NSCreationTimeDocumentAttribute](../AppKit/nscreationtimedocumentattribute.md)
  The creation date of the document.
- [NSEditorDocumentAttribute](../AppKit/nseditordocumentattribute.md)
  The name of person who last edited the document.
- [NSKeywordsDocumentAttribute](../AppKit/nskeywordsdocumentattribute.md)
  The document keywords.
- [NSManagerDocumentAttribute](../AppKit/nsmanagerdocumentattribute.md)
  The name of the author’s manager.
- [NSModificationTimeDocumentAttribute](../AppKit/nsmodificationtimedocumentattribute.md)
  The modification date of the document.
- [NSReadOnlyDocumentAttribute](./nsreadonlydocumentattribute.md)
  An indication of whether the document is read-only.
- [NSSubjectDocumentAttribute](../AppKit/nssubjectdocumentattribute.md)
  The subject of the document.
- [NSTitleDocumentAttribute](../AppKit/nstitledocumentattribute.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscharacterencodingdocumentattribute)*