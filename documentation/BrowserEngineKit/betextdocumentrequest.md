# BETextDocumentRequest

**Framework**: BrowserEngineKit  
**Kind**: class

A description of the contextual information that a text document request retrieves.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class BETextDocumentRequest
```

#### Overview

The [`BETextInput`](betextinput.md) protocol’s [`requestDocumentContext(_:completionHandler:)`](betextinput/requestdocumentcontext(_:completionhandler:).md) and [`selectPosition(at:for:completionHandler:)`](betextinput/selectposition(at:for:completionhandler:).md) methods take an instance of this class as an argument.

## Topics

### Scoping the document request
- [var surroundingGranularity: UITextGranularity](betextdocumentrequest/surroundinggranularity.md)
  The unit of measurement for the document request’s scope.
- [var granularityCount: Int](betextdocumentrequest/granularitycount.md)
  A count of granularity units that defines the scope of the document request.
### Specifying the requested information
- [var options: BETextDocumentRequest.Options](betextdocumentrequest/options-swift.property.md)
  A set of options that describes the contextual information the system requests from the document.
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
  Options that describe the contextual information for a text document request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
  A suggestion object that provides AutoFill text content for web form fields based on a person’s usage patterns.
- [class BETextAlternatives](betextalternatives.md)
  An object that provides alternative text suggestions for a person’s text selection.
- [class BETextDocumentContext](betextdocumentcontext.md)
  Information about the text surrounding a selection in a document.
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
  Options that describe the contextual information for a text document request.
- [class BETextSuggestion](betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentrequest)*