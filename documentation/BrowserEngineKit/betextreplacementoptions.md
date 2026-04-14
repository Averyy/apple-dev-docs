# BETextReplacementOptions

**Framework**: BrowserEngineKit  
**Kind**: struct

Options that determine the way your app processes text in webpages.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
struct BETextReplacementOptions
```

#### Overview

The [`BETextInput`](betextinput.md) protocol’s [`replaceText(_:withText:options:completionHandler:)`](betextinput/replacetext(_:withtext:options:completionhandler:).md) method takes in instance of this structure as an argument.

## Topics

### Identifying text-replacement options
- [static var addUnderline: BETextReplacementOptions](betextreplacementoptions/addunderline.md)
  An option that processes text by adding an underline to its visual style.
### Creating text-replacement options
- [init(rawValue: UInt)](betextreplacementoptions/init(rawvalue:).md)
  Creates a text-replacement option with the specified underlying value.

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
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
  Options that describe the contextual information for a text document request.
- [class BETextSuggestion](betextsuggestion.md)
  A text suggestion to insert into a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextreplacementoptions)*