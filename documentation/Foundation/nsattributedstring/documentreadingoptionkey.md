# NSAttributedString.DocumentReadingOptionKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

## Overview

The [`NSAttributedString.DocumentReadingOptionKey`](./documentreadingoptionkey.md) type defines attributes to use when creating an attributed string from data in a file. Use these strings with methods such as [`init(data:options:documentAttributes:)`](./init%28data,options,documentattributes%29.md), [`init(HTML:options:documentAttributes:)`](./init%28html,options,documentattributes%29.md), [`init(URL:options:documentAttributes:)`](./init%28url,options,documentattributes%29.md), [`read(from:options:documentAttributes:)`](../nsmutableattributedstring/read%28from,options,documentattributes%29-5mbcx.md), and [`read(from:options:documentAttributes:)`](../nsmutableattributedstring/read%28from,options,documentattributes%29-54wth.md) to specify expected details. For example, specify the [`documentType`](./documentreadingoptionkey/documenttype.md) attribute to interpret the file data as a specific file format.

## Topics

### Getting the document options
- [static let baseURL: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/baseurl.md)
  The base URL for HTML documents.
- [static let characterEncoding: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/characterencoding.md)
  The string encoding.
- [static let defaultAttributes: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/defaultattributes.md)
  The default attributes to apply to plain files.
- [static let documentType: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/filetype.md)
  The file type.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/readaccessurl.md)
  The local files WebKit can access when loading content.
- [static let textEncodingName: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/textencodingname.md)
  The text encoding to use.
- [static let textSizeMultiplier: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/textsizemultiplier.md)
  The scale factor for font sizes.
- [static let timeout: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/timeout.md)
  The time, in seconds, to wait for a document to finish loading.
- [static let webPreferences: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/webpreferences.md)
  A WebPreferences object.
- [static let webResourceLoadDelegate: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/webresourceloaddelegate.md)
  An object to serve as the web resource loading delegate.
### Getting the font-scaling options
- [static let sourceTextScaling: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/sourcetextscaling.md)
  The text-scaling mode to associate with the document’s content.
- [static let targetTextScaling: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/targettextscaling.md)
  The text scaling mode to use after reading the text from disk.
### Initializers
- [init(String)](./documentreadingoptionkey/init%28_%29.md)
  Creates a document reading option key with the specified raw value.
- [init(rawValue: String)](./documentreadingoptionkey/init%28rawvalue%29.md)
  Creates a document reading option key with the specified raw value.
### Type Properties
- [static let textKit1ListMarkerFormatDocumentOption: NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey/textkit1listmarkerformatdocumentoption.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting document-wide attributes
- [NSAttributedString.DocumentAttributeKey](./documentattributekey.md)
  The attributes you apply to an entire document.
- [HTML attributes](../html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](./documenttype.md)
  Constants for the document type document attribute key.
- [NSAttributedString.TextLayoutSectionKey](./textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../../UIKit/nstextscalingtype.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey)*