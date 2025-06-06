# BETextSuggestion

**Framework**: BrowserEngineKit  
**Kind**: class

A text suggestion to insert into a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class BETextSuggestion
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Overview

You typically don’t create instances of `BETextSuggestion`. The system supplies them to your browser text view’s [`insert(_:)`](betextinput/insert(_:)-5iryn.md) method to suggest text insertions, for example AutoFill suggestions.

## Topics

### Creating a text suggestion
- [init(inputText: String)](betextsuggestion/init(inputtext:).md)
  Initializes a new text suggestion with the given input text.
### Getting the suggested text
- [var inputText: String](betextsuggestion/inputtext.md)
  Text that will be inserted into the document when the user chooses the suggestion.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
- [class BETextAlternatives](betextalternatives.md)
- [class BETextDocumentContext](betextdocumentcontext.md)
  Information about the text surrounding a selection in a document.
- [class BETextDocumentRequest](betextdocumentrequest.md)
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
- [struct BETextReplacementOptions](betextreplacementoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextsuggestion)*