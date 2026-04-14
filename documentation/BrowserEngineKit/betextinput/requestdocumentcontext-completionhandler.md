# requestDocumentContext(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Gathers context for the system about the current document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestDocumentContext(_ request: BETextDocumentRequest) async -> BETextDocumentContext
```

## See Also

- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](betextinput/requesttextcontextforautocorrection(completionhandler:).md)
  A method the text system calls to get extra information for autocorrection suggestions.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](betextinput/requesttextrects(for:withcompletionhandler:).md)
  Gathers context for the presentation of a text-related user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requestdocumentcontext(_:completionhandler:))*