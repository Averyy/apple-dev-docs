# NSAttributedString.DocumentReadingOptionKey

**Framework**: Foundation  
**Kind**: struct

Options for constructing an attributed string from data you read from disk.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct DocumentReadingOptionKey
```

#### Overview

The [`NSAttributedString.DocumentReadingOptionKey`](nsattributedstring/documentreadingoptionkey.md) type defines attributes to use when creating an attributed string from data in a file. Use these strings with methods such as [`init(data:options:documentAttributes:)`](nsattributedstring/init(data:options:documentattributes:).md), [`init(HTML:options:documentAttributes:)`](nsattributedstring/init(html:options:documentattributes:).md), [`init(URL:options:documentAttributes:)`](nsattributedstring/init(url:options:documentattributes:).md), [`read(from:options:documentAttributes:)`](nsmutableattributedstring/read(from:options:documentattributes:)-5mbcx.md), and [`read(from:options:documentAttributes:)`](nsmutableattributedstring/read(from:options:documentattributes:)-54wth.md) to specify expected details. For example, specify the [`documentType`](nsattributedstring/documentreadingoptionkey/documenttype.md) attribute to interpret the file data as a specific file format.

## Topics

### Getting the document options
- [static let baseURL: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/baseurl.md)
  The base URL for HTML documents.
- [static let characterEncoding: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/characterencoding.md)
  The string encoding.
- [static let defaultAttributes: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/defaultattributes.md)
  The default attributes to apply to plain files.
- [static let documentType: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/filetype.md)
  The file type.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/readaccessurl.md)
  The local files WebKit can access when loading content.
- [static let textEncodingName: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/textencodingname.md)
  The text encoding to use.
- [static let textSizeMultiplier: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/textsizemultiplier.md)
  The scale factor for font sizes.
- [static let timeout: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/timeout.md)
  The time, in seconds, to wait for a document to finish loading.
- [static let webPreferences: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/webpreferences.md)
  A WebPreferences object.
- [static let webResourceLoadDelegate: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/webresourceloaddelegate.md)
  An object to serve as the web resource loading delegate.
### Getting the font-scaling options
- [static let sourceTextScaling: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/sourcetextscaling.md)
  The text-scaling mode to associate with the document’s content.
- [static let targetTextScaling: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/targettextscaling.md)
  The text scaling mode to use after reading the text from disk.
### Initializers
- [init(String)](nsattributedstring/documentreadingoptionkey/init(_:).md)
  Creates a document reading option key with the specified raw value.
- [init(rawValue: String)](nsattributedstring/documentreadingoptionkey/init(rawvalue:).md)
  Creates a document reading option key with the specified raw value.
### Type Properties
- [static let textKit1ListMarkerFormatDocumentOption: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/textkit1listmarkerformatdocumentoption.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey.md)
  The attributes you apply to an entire document.
- [HTML attributes](html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](nsattributedstring/documenttype.md)
  Constants for the document type document attribute key.
- [NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../UIKit/NSTextScalingType.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey)*