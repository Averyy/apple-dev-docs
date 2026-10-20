# NSAttributedString.DocumentAttributeKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

The [`NSAttributedString.DocumentAttributeKey`](./documentattributekey.md) type defines attributes that apply to an entire attributed string, and not to specific ranges of characters. You specify these attributes when writing an attributed string to disk, or reading text from a file on disk. Use these attributes to specify metadata about the overall document, including its author or title, page margin details, font-scaling options for cross-platform interchange, and more.

## Topics

### Getting document type keys
- [static let documentType: NSAttributedString.DocumentAttributeKey](./documentattributekey/documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentAttributeKey](./documentattributekey/filetype.md)
  The document type for interpreting the document.
- [static let textEncodingName: NSAttributedString.DocumentAttributeKey](./documentattributekey/textencodingname.md)
  The name of the text encoding to use.
### Getting document metadata keys
- [static let author: NSAttributedString.DocumentAttributeKey](./documentattributekey/author.md)
  The author of the document.
- [static let category: NSAttributedString.DocumentAttributeKey](./documentattributekey/category.md)
  The document’s category.
- [static let characterEncoding: NSAttributedString.DocumentAttributeKey](./documentattributekey/characterencoding.md)
  The string encoding for the document.
- [static let cocoaVersionDocumentAttribute: NSAttributedString.DocumentAttributeKey](./documentattributekey/cocoaversiondocumentattribute.md)
  The version of Cocoa that created the file.
- [static let comment: NSAttributedString.DocumentAttributeKey](./documentattributekey/comment.md)
  The document comments.
- [static let company: NSAttributedString.DocumentAttributeKey](./documentattributekey/company.md)
  The company or organization name associated with the document.
- [static let converted: NSAttributedString.DocumentAttributeKey](./documentattributekey/converted.md)
  A value that indicates whether a filter service converted the file.
- [static let copyright: NSAttributedString.DocumentAttributeKey](./documentattributekey/copyright.md)
  The document’s copyright information.
- [static let creationTime: NSAttributedString.DocumentAttributeKey](./documentattributekey/creationtime.md)
  The creation date of the document.
- [static let editor: NSAttributedString.DocumentAttributeKey](./documentattributekey/editor.md)
  The name of person who last edited the document.
- [static let keywords: NSAttributedString.DocumentAttributeKey](./documentattributekey/keywords.md)
  The document keywords.
- [static let manager: NSAttributedString.DocumentAttributeKey](./documentattributekey/manager.md)
  The name of the author’s manager.
- [static let modificationTime: NSAttributedString.DocumentAttributeKey](./documentattributekey/modificationtime.md)
  The modification date of the document.
- [static let readOnly: NSAttributedString.DocumentAttributeKey](./documentattributekey/readonly.md)
  An indication of whether the document is read-only.
- [static let subject: NSAttributedString.DocumentAttributeKey](./documentattributekey/subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](./documentattributekey/title.md)
  The document title.
### Getting document appearance keys
- [static let appearance: NSAttributedString.DocumentAttributeKey](./documentattributekey/appearance.md)
  The appearance of the document.
- [static let backgroundColor: NSAttributedString.DocumentAttributeKey](./documentattributekey/backgroundcolor.md)
  The background color of the document.
- [static let bottomMargin: NSAttributedString.DocumentAttributeKey](./documentattributekey/bottommargin.md)
  The bottom margin of the document.
- [static let defaultFontExcluded: NSAttributedString.DocumentAttributeKey](./documentattributekey/defaultfontexcluded.md)
- [static let defaultTabInterval: NSAttributedString.DocumentAttributeKey](./documentattributekey/defaulttabinterval.md)
  The default tab stop interval for the document.
- [static let excludedElements: NSAttributedString.DocumentAttributeKey](./documentattributekey/excludedelements.md)
  The HTML elements to exclude in generated HTML.
- [static let hyphenationFactor: NSAttributedString.DocumentAttributeKey](./documentattributekey/hyphenationfactor.md)
  The hyphenation factor of the document.
- [static let leftMargin: NSAttributedString.DocumentAttributeKey](./documentattributekey/leftmargin.md)
  The left margin of the document.
- [static let paperMargin: NSAttributedString.DocumentAttributeKey](./documentattributekey/papermargin.md)
  The paper margin of the document.
- [static let paperSize: NSAttributedString.DocumentAttributeKey](./documentattributekey/papersize.md)
  The paper size for the document.
- [static let prefixSpaces: NSAttributedString.DocumentAttributeKey](./documentattributekey/prefixspaces.md)
  The number of spaces for indenting nested HTML elements.
- [static let rightMargin: NSAttributedString.DocumentAttributeKey](./documentattributekey/rightmargin.md)
  The right margin of the document.
- [static let textLayoutSections: NSAttributedString.DocumentAttributeKey](./documentattributekey/textlayoutsections.md)
  The layout orientations for each section.
- [static let topMargin: NSAttributedString.DocumentAttributeKey](./documentattributekey/topmargin.md)
  The top margin of the document.
- [static let viewMode: NSAttributedString.DocumentAttributeKey](./documentattributekey/viewmode.md)
  The view mode.
- [static let viewSize: NSAttributedString.DocumentAttributeKey](./documentattributekey/viewsize.md)
  The view size.
- [static let viewZoom: NSAttributedString.DocumentAttributeKey](./documentattributekey/viewzoom.md)
  The view zoom.
### Getting the font-scaling options
- [static let sourceTextScaling: NSAttributedString.DocumentAttributeKey](./documentattributekey/sourcetextscaling.md)
  The text-scaling mode you used when creating the text.
- [static let textScaling: NSAttributedString.DocumentAttributeKey](./documentattributekey/textscaling.md)
  The text-scaling mode to use when displaying the text.
### Getting the default attributes
- [static let defaultAttributes: NSAttributedString.DocumentAttributeKey](./documentattributekey/defaultattributes.md)
  The default document attributes.
### Initializers
- [init(String)](./documentattributekey/init%28_%29.md)
  Creates a document attribute key.
- [init(rawValue: String)](./documentattributekey/init%28rawvalue%29.md)
  Creates a document attribute key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting document-wide attributes
- [NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [HTML attributes](../html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](./documenttype.md)
  Constants for the document type document attribute key.
- [NSAttributedString.TextLayoutSectionKey](./textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../../UIKit/nstextscalingtype.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey)*