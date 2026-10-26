# NSCocoaVersionDocumentAttribute

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The version of Cocoa that created the file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey const NSCocoaVersionDocumentAttribute;
```

#### Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing a float. For RTF files only, stores the version of Cocoa with which the file was created. Absence of this value indicates an RTF file was not created by Cocoa or its predecessors.

Values less than `100` are pre–macOS; `100` is macOS 10.0 or 10.1; `102` is macOS 10.2 and 10.3; values greater than `102` correspond to values of `NSAppKitVersionNumber` in macOS 10.4 and later.

The string constant in macOS 10.3 and earlier is `@"CocoaRTFVersion"`.

## See Also

### Getting document metadata keys
- [NSAuthorDocumentAttribute](../AppKit/nsauthordocumentattribute.md)
  The author of the document.
- [NSCategoryDocumentAttribute](../AppKit/nscategorydocumentattribute.md)
  The document’s category.
- [NSCharacterEncodingDocumentAttribute](./nscharacterencodingdocumentattribute.md)
  The string encoding for the document.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscocoaversiondocumentattribute)*