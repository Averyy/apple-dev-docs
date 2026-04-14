# requestTextContextForAutocorrection(completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

A method the text system calls to get extra information for autocorrection suggestions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestTextContextForAutocorrection() async -> BETextDocumentContext
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

The system calls this method to retrieve extra context for the currently selected text.

Construct a [`BETextDocumentContext`](betextdocumentcontext.md) that contains complete sentences that also include the current selection. If the selection is at a sentence boundary, also include the preceding sentence.

## Parameters

- `completionHandler`: A closure that you call to supply the context as a [`BETextDocumentContext`](betextdocumentcontext.md).

## See Also

- [func requestDocumentContext(BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](betextinput/requestdocumentcontext(_:completionhandler:).md)
  Gathers context for the system about the current document.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](betextinput/requesttextrects(for:withcompletionhandler:).md)
  Gathers context for the presentation of a text-related user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requesttextcontextforautocorrection(completionhandler:))*