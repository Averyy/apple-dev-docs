# BETextAlternatives

**Framework**: BrowserEngineKit  
**Kind**: class

An object that provides alternative text suggestions for a person’s text selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class BETextAlternatives
```

#### Overview

The [`BETextInput`](betextinput.md) protocol provides your app an instance of this class as an argument to the  [`alternativesForSelectedText()`](betextinput/alternativesforselectedtext().md) callback.

## Topics

### Considering alternative text
- [var alternativeStrings: [String]](betextalternatives/alternativestrings.md)
  An array of strings that represent alternatives to the currently selected text.
### Reviewing the source text
- [var primaryString: String](betextalternatives/primarystring.md)
  The original text that the alternatives derive from.

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
- [class BETextDocumentContext](betextdocumentcontext.md)
  Information about the text surrounding a selection in a document.
- [class BETextDocumentRequest](betextdocumentrequest.md)
  A description of the contextual information that a text document request retrieves.
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
  Options that describe the contextual information for a text document request.
- [class BETextSuggestion](betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextalternatives)*