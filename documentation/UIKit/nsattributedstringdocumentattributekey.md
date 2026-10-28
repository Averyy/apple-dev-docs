# NSAttributedStringDocumentAttributeKey

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The attributes you apply to an entire document.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
typedef NSString * NSAttributedStringDocumentAttributeKey;
```

## Discussion

The [`NSAttributedStringDocumentAttributeKey`](./nsattributedstringdocumentattributekey.md) type defines attributes that apply to an entire attributed string, and not to specific ranges of characters. You specify these attributes when writing an attributed string to disk, or reading text from a file on disk. Use these attributes to specify metadata about the overall document, including its author or title, page margin details, font-scaling options for cross-platform interchange, and more.

## Topics

### Getting document type keys
- [NSDocumentTypeDocumentAttribute](./nsdocumenttypedocumentattribute.md)
  The document type.
- [NSFileTypeDocumentAttribute](../AppKit/nsfiletypedocumentattribute.md)
  The document type for interpreting the document.
- [NSTextEncodingNameDocumentAttribute](../AppKit/nstextencodingnamedocumentattribute.md)
  The name of the text encoding to use.
### Getting document metadata keys
- [NSAuthorDocumentAttribute](../AppKit/nsauthordocumentattribute.md)
  The author of the document.
- [NSCategoryDocumentAttribute](../AppKit/nscategorydocumentattribute.md)
  The document’s category.
- [NSCharacterEncodingDocumentAttribute](./nscharacterencodingdocumentattribute.md)
  The string encoding for the document.
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
### Getting document appearance keys
- [NSAppearanceDocumentAttribute](../AppKit/nsappearancedocumentattribute.md)
  The appearance of the document.
- [NSBackgroundColorDocumentAttribute](./nsbackgroundcolordocumentattribute.md)
  The background color of the document.
- [NSBottomMarginDocumentAttribute](../AppKit/nsbottommargindocumentattribute.md)
  The bottom margin of the document.
- [NSDefaultFontExcludedDocumentAttribute](./nsdefaultfontexcludeddocumentattribute.md)
- [NSDefaultTabIntervalDocumentAttribute](./nsdefaulttabintervaldocumentattribute.md)
  The default tab stop interval for the document.
- [NSExcludedElementsDocumentAttribute](../AppKit/nsexcludedelementsdocumentattribute.md)
  The HTML elements to exclude in generated HTML.
- [NSHyphenationFactorDocumentAttribute](./nshyphenationfactordocumentattribute.md)
  The hyphenation factor of the document.
- [NSLeftMarginDocumentAttribute](../AppKit/nsleftmargindocumentattribute.md)
  The left margin of the document.
- [NSPaperMarginDocumentAttribute](./nspapermargindocumentattribute.md)
  The paper margin of the document.
- [NSPaperSizeDocumentAttribute](./nspapersizedocumentattribute.md)
  The paper size for the document.
- [NSPrefixSpacesDocumentAttribute](../AppKit/nsprefixspacesdocumentattribute.md)
  The number of spaces for indenting nested HTML elements.
- [NSRightMarginDocumentAttribute](../AppKit/nsrightmargindocumentattribute.md)
  The right margin of the document.
- [NSTextLayoutSectionsAttribute](./nstextlayoutsectionsattribute.md)
  The layout orientations for each section.
- [NSTopMarginDocumentAttribute](../AppKit/nstopmargindocumentattribute.md)
  The top margin of the document.
- [NSViewModeDocumentAttribute](./nsviewmodedocumentattribute.md)
  The view mode.
- [NSViewSizeDocumentAttribute](./nsviewsizedocumentattribute.md)
  The view size.
- [NSViewZoomDocumentAttribute](./nsviewzoomdocumentattribute.md)
  The view zoom.
### Getting the font-scaling options
- [NSSourceTextScalingDocumentAttribute](./nssourcetextscalingdocumentattribute.md)
  The text-scaling mode you used when creating the text.
- [NSTextScalingDocumentAttribute](./nstextscalingdocumentattribute.md)
  The text-scaling mode to use when displaying the text.
### Getting the default attributes
- [NSDefaultAttributesDocumentAttribute](./nsdefaultattributesdocumentattribute.md)
  The default document attributes.

## See Also

### Getting document-wide attributes
- [Document reading option keys](./document-reading-option-keys.md)
  Keys for constructing an attributed string from data on disk.
- [NSAttributedStringDocumentType](./nsattributedstringdocumenttype.md)
  Constants for the document type document attribute key.
- [NSTextLayoutSectionKey](./nstextlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](./nstextscalingtype.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsattributedstringdocumentattributekey)*