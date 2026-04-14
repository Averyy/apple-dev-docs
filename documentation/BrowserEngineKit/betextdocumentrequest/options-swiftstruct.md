# BETextDocumentRequest.Options

**Framework**: BrowserEngineKit  
**Kind**: struct

Options that describe the contextual information for a text document request.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
struct Options
```

## Topics

### Creating an options structure
- [init(rawValue: Int)](betextdocumentrequest/options-swift.struct/init(rawvalue:).md)
  Initializes an options instance for a text document request with the specified raw value.
### Accessing text content
- [static var text: BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct/text.md)
  An option that requests the plaintext content of the document.
- [static var attributedText: BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct/attributedtext.md)
  An option that requests the document’s text content along with its formatting and style attributes.
### Getting geometric information
- [static var textRects: BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct/textrects.md)
  An option that requests the rectangular bounds of text within a document’s layout.
- [static var markedTextRects: BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct/markedtextrects.md)
  An option that requests the rectangular bounds of marked text regions.
### Getting correction information
- [static var autocorrectedRanges: BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct/autocorrectedranges.md)
  An option that requests the ranges of text the system autocorrects within the document.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
  A suggestion object that provides AutoFill text content for web form fields based on a person’s usage patterns.
- [class BETextAlternatives](betextalternatives.md)
  An object that provides alternative text suggestions for a person’s text selection.
- [class BETextDocumentContext](betextdocumentcontext.md)
  Information about the text surrounding a selection in a document.
- [class BETextDocumentRequest](betextdocumentrequest.md)
  A description of the contextual information that a text document request retrieves.
- [class BETextSuggestion](betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentrequest/options-swift.struct)*