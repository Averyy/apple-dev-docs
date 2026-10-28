# requestTextContextForAutocorrection(completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A method the text system calls to get extra information for autocorrection suggestions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestTextContextForAutocorrection(completionHandler: @escaping @Sendable (BETextDocumentContext) -> Void)
```

```swift
func requestTextContextForAutocorrection() async -> BETextDocumentContext
```

```objc
- (void) requestTextContextForAutocorrectionWithCompletionHandler:(void (^)(BETextDocumentContext *context)) completionHandler;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## Discussion

The system calls this method to retrieve extra context for the currently selected text.

Construct a [`BETextDocumentContext`](../betextdocumentcontext.md) that contains complete sentences that also include the current selection. If the selection is at a sentence boundary, also include the preceding sentence.

## Parameters

- `completionHandler`: A closure that you call to supply the context as a [`BETextDocumentContext`](../betextdocumentcontext.md).

## See Also

### Requesting context
- [func requestDocumentContext(BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./requestdocumentcontext%28_,completionhandler%29.md)
  Gathers context for the system about the current document.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](./requesttextrects%28for,withcompletionhandler%29.md)
  Gathers context for the presentation of a text-related user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requesttextcontextforautocorrection(completionhandler:))*