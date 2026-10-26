# BETextDocumentRequest.Options

**Framework**: BrowserEngineKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum BETextDocumentRequestOptions : NSInteger;
```

## Topics

### Creating an options structure
- [init(rawValue: Int)](./options-swift.struct/init%28rawvalue%29.md)
  Initializes an options instance for a text document request with the specified raw value.
### Accessing text content
- [static var text: BETextDocumentRequest.Options](./options-swift.struct/text.md)
  An option that requests the plaintext content of the document.
- [static var attributedText: BETextDocumentRequest.Options](./options-swift.struct/attributedtext.md)
  An option that requests the document’s text content along with its formatting and style attributes.
### Getting geometric information
- [static var textRects: BETextDocumentRequest.Options](./options-swift.struct/textrects.md)
  An option that requests the rectangular bounds of text within a document’s layout.
- [static var markedTextRects: BETextDocumentRequest.Options](./options-swift.struct/markedtextrects.md)
  An option that requests the rectangular bounds of marked text regions.
### Getting correction information
- [static var autocorrectedRanges: BETextDocumentRequest.Options](./options-swift.struct/autocorrectedranges.md)
  An option that requests the ranges of text the system autocorrects within the document.
### Specifying no options
- [BETextDocumentOptionNone](../betextdocumentrequestoptions/betextdocumentoptionnone.md)
  An option that specifies no information to request for the text document.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Replacements and AutoFill
- [class BEAutoFillTextSuggestion](../beautofilltextsuggestion.md)
  A suggestion object that provides AutoFill text content for web form fields based on a person’s usage patterns.
- [class BETextAlternatives](../betextalternatives.md)
  An object that provides alternative text suggestions for a person’s text selection.
- [class BETextDocumentContext](../betextdocumentcontext.md)
  Information about the text surrounding a selection in a document.
- [class BETextDocumentRequest](../betextdocumentrequest.md)
  A description of the contextual information that a text document request retrieves.
- [class BETextSuggestion](../betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](../betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentrequest/options-swift.struct)*