# requestTextRects(for:withCompletionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Gathers context for the presentation of a text-related user interface.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestTextRects(for input: String) async -> [UITextSelectionRect]
```

#### Discussion

The system invokes your implementation of this method. The completion handler receives [`UITextSelectionRect`](https://developer.apple.com/documentation/UIKit/UITextSelectionRect) instances for the substring nearest to the caret that matches the given `input`.

## See Also

- [func requestDocumentContext(BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](betextinput/requestdocumentcontext(_:completionhandler:).md)
  Gathers context for the system about the current document.
- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](betextinput/requesttextcontextforautocorrection(completionhandler:).md)
  A method the text system calls to get extra information for autocorrection suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requesttextrects(for:withcompletionhandler:))*