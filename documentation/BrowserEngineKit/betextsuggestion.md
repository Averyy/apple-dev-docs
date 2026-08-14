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

Don’t create instances of this class. The system provides instances to your app through a text view’s [`insert(_:)`](betextinput/insert(_:)-5iryn.md) method when it suggests text insertions, for example, an AutoFill suggestion.

## Topics

### Creating a text suggestion
- [init(inputText: String)](betextsuggestion/init(inputtext:).md)
  Initializes a new text suggestion with the given input text.
### Getting the suggested text
- [var inputText: String](betextsuggestion/inputtext.md)
  Text that will be inserted into the document when the user chooses the suggestion.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

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
- [struct BETextReplacementOptions](betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextsuggestion)*