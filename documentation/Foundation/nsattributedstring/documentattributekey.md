# NSAttributedString.DocumentAttributeKey

**Framework**: Foundation  
**Kind**: struct

The attributes you apply to an entire document.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct DocumentAttributeKey
```

#### Overview

The [`NSAttributedString.DocumentAttributeKey`](nsattributedstring/documentattributekey.md) type defines attributes that apply to an entire attributed string, and not to specific ranges of characters. You specify these attributes when writing an attributed string to disk, or reading text from a file on disk. Use these attributes to specify metadata about the overall document, including its author or title, page margin details, font-scaling options for cross-platform interchange, and more.

## Topics

### Getting document type keys
- [static let documentType: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/filetype.md)
  The document type for interpreting the document.
- [static let textEncodingName: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/textencodingname.md)
  The name of the text encoding to use.
### Getting document metadata keys
- [static let author: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/author.md)
  The author of the document.
- [static let category: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/category.md)
  The document’s category.
- [static let characterEncoding: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/characterencoding.md)
  The string encoding for the document.
- [static let comment: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/comment.md)
  The document comments.
- [static let company: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/company.md)
  The company or organization name associated with the document.
- [static let converted: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/converted.md)
  A value that indicates whether a filter service converted the file.
- [static let copyright: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/copyright.md)
  The document’s copyright information.
- [static let creationTime: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/creationtime.md)
  The creation date of the document.
- [static let editor: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/editor.md)
  The name of person who last edited the document.
- [static let keywords: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/keywords.md)
  The document keywords.
- [static let manager: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/manager.md)
  The name of the author’s manager.
- [static let modificationTime: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/modificationtime.md)
  The modification date of the document.
- [static let readOnly: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/readonly.md)
  An indication of whether the document is read-only.
- [static let subject: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/title.md)
  The document title.
### Getting document appearance keys
- [static let appearance: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/appearance.md)
  The appearance of the document.
- [static let backgroundColor: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/backgroundcolor.md)
  The background color of the document.
- [static let bottomMargin: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/bottommargin.md)
  The bottom margin of the document.
- [static let defaultFontExcluded: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/defaultfontexcluded.md)
- [static let defaultTabInterval: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/defaulttabinterval.md)
  The default tab stop interval for the document.
- [static let excludedElements: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/excludedelements.md)
  The HTML elements to exclude in generated HTML.
- [static let hyphenationFactor: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/hyphenationfactor.md)
  The hyphenation factor of the document.
- [static let leftMargin: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/leftmargin.md)
  The left margin of the document.
- [static let paperMargin: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/papermargin.md)
  The paper margin of the document.
- [static let paperSize: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/papersize.md)
  The paper size for the document.
- [static let prefixSpaces: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/prefixspaces.md)
  The number of spaces for indenting nested HTML elements.
- [static let rightMargin: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/rightmargin.md)
  The right margin of the document.
- [static let textLayoutSections: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/textlayoutsections.md)
  The layout orientations for each section.
- [static let topMargin: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/topmargin.md)
  The top margin of the document.
- [static let viewMode: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/viewmode.md)
  The view mode.
- [static let viewSize: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/viewsize.md)
  The view size.
- [static let viewZoom: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/viewzoom.md)
  The view zoom.
### Getting the font-scaling options
- [static let sourceTextScaling: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/sourcetextscaling.md)
  The text-scaling mode you used when creating the text.
- [static let textScaling: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/textscaling.md)
  The text-scaling mode to use when displaying the text.
### Getting the default attributes
- [static let defaultAttributes: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/defaultattributes.md)
  The default document attributes.
### Initializers
- [init(String)](nsattributedstring/documentattributekey/init(_:).md)
  Creates a document attribute key.
- [init(rawValue: String)](nsattributedstring/documentattributekey/init(rawvalue:).md)
  Creates a document attribute key with the specified raw value.
### Type Properties
- [static let cocoaVersionDocumentAttribute: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/cocoaversion.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [HTML attributes](html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](nsattributedstring/documenttype.md)
  Constants for the document type document attribute key.
- [NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../UIKit/NSTextScalingType.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey)*